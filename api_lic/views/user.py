# from falcon_rest.db import fields, orm , get_db
import csv
import falcon
import io
import json
from datetime import datetime, timedelta
from time import mktime
import jwt
from dateutil.parser import parse as parse_datetime
from pytz import UTC
from urllib.parse import parse_qsl, urlencode
# from falcon_rest.db import Column
# from falcon_rest.conf import settings
# from falcon_rest.contrib.files import create_file_model_class, create_scheme
# from falcon_rest.contrib.files.endpoints import UploadFile, GetDownloadLink, DownloadFile, ShowFile
# from marshmallow_sqlalchemy import field_for, fields as sa
from sqlalchemy import (desc)
from sqlalchemy import text as text_, and_, or_
from sqlalchemy.sql import func, select

# from api_dnl.base_model import DnlApiBaseModel
# from api_dnl.model import rev

from falcon_rest import schemes, resources, responses
from falcon_rest.db.errors import IntegrityError, FkConstraintViolation, NoResultFound
from falcon_rest.helpers import check_permission, get_request_ip
from falcon_rest.logger import log
from falcon_rest.resources.resources import swagger, ResourcesBaseClass, ATTRIBUTE_ERROR_RE
from falcon_rest.responses import errors, SuccessResponseObjectInfo
# from .tasks import *
from api_lic import model
from api_lic import settings
from .auth import DEFAULT_SECURITY
from ..scheme import *
from ..scheme import _valid
from ..resources.resources import Create, Resource, List, CustomAction, CustomPostAction, CustomPatchAction, \
	OperationalError
from ..rbac.rbac_role import UserRole, AdminRole
import paypalrestsdk
import stripe


class UserInfoResource(Resource):
	model_class = model.User
	scheme_class = UserInfoScheme
	scheme_class_get = UserInfoSchemeGet
	scheme_class_modify = UserInfoSchemeModify
	entity = 'User'
	unique_field = 'email'
	has_delete_operation = False
	security = (DEFAULT_SECURITY)
	restrict = ()

	def on_get(self, req, resp, **kwargs):
		kwargs['user_uuid'] = self.get_user(req).user_uuid

		return super(UserInfoResource, self).on_get(req, resp, **kwargs)

	def on_patch(self, req, resp, **kwargs):
		kwargs['user_uuid'] = self.get_user(req).user_uuid
		return super(UserInfoResource, self).on_patch(req, resp, **kwargs)


class UserResetPasswordEmail(CustomAction):
	scheme_class = UserResetPasswordLetterScheme
	body_parameters = ('Email to check', UserResetPasswordLetterScheme)
	method = 'post'
	model_class = model.User

	def on_post(self, req, resp, **kwargs):
		return self.proceed(req, resp, **kwargs)

	def apply(self, obj, req, resp, **kwargs):
		from falcon_rest.contrib.auth import auth
		user = model.User.filter(email=req.data['email']).first()
		if user:
			user.token = auth.get_token(user)
			ret = user.apply_mail('retrieve_password')
			if ret:
				self.set_response(resp, responses.OperationErrorResponse(
					data=dict(message=ret, reason='mail_error', code=406)))
				return False
		# model.MailSender.apply_mail(user, 'retrieve_password', obj.client.billing_email)


class NotificationList(List):
	scheme_class = NotificationSchemeGet
	model_class = model.Notification
	entity_plural = 'Notifications'
	path_parameters = ()
	security = (DEFAULT_SECURITY)
	restrict = ()

	def modify_query_from_filtering_for_list(self, filtering, **kwargs):
		filt, ret = super().modify_query_from_filtering_for_list(filtering, **kwargs)
		user = self.get_user(self.req)
		if user.get_role() != AdminRole:
			cls = self.model_class
			ret = ret.filter(cls.user_uuid == user.user_uuid)
		return filt, ret


class PaymentCreate(Create):
	scheme_class = PaymentScheme
	model_class = model.Payment
	entity = 'Payment'
	path_parameters = ()
	security = (DEFAULT_SECURITY)
	restrict = ()

	def before_create(self, obj, **kwargs):
		user = self.get_user(self.req)
		if not obj.user_uuid:
			obj.user_uuid = user.user_uuid
		if obj.license_lrn_uuid:
			lic = model.LicenseLrn.get(obj.license_lrn_uuid)
			if not lic:
				raise ValidationError({'license_switch_uuid': ['no such LRN license uuid!']})
			if lic and lic.user_uuid != user.user_uuid:
				raise ValidationError({'license_lrn_uuid': ['not owned by current user!']})
			if lic.amount and (not obj.amount_lrn or obj.amount_lrn < lic.amount * lic.dur_months):
				raise ValidationError({'amount_lrn': [
					'not valid. must be equal or more than package price {}'.format(lic.amount * lic.dur_months)]})
			hist = lic.add_history(obj.type)
			if hist:
				obj.session().add(hist)

		if obj.license_switch_uuid:
			lic = model.LicenseSwitch.get(obj.license_switch_uuid)

			if not lic:
				raise ValidationError({'license_switch_uuid': ['no such switch license uuid!']})
			if lic and lic.user_uuid != user.user_uuid:
				raise ValidationError({'license_switch_uuid': ['not owned by current user!']})
			if lic.amount and (not obj.amount_switch or obj.amount_switch < lic.amount * lic.dur_months):
				raise ValidationError({'amount_swich': [
					'not valid. must be equal or more than package price {}'.format(lic.amount * lic.dur_months)]})
			hist = lic.add_history(obj.type)
			if hist:
				obj.session().add(hist)

		# obj.created_by=user.name
		# obj.created_on=datetime.now(UTC)

		return obj

	def after_create(self, object_id, req, resp, **kwargs):
		obj = self.model_class.get(object_id)
		if obj.user.alert_payment_received:
			ret = obj.apply_mail('payment_received')


class PaymentResource(Resource):
	model_class = model.Payment
	scheme_class = PaymentScheme
	scheme_class_get = PaymentSchemeGet
	scheme_class_modify = PaymentSchemeModify
	entity = 'Payment'
	id_field = 'payment_uuid'
	security = (DEFAULT_SECURITY)
	path_parameters = ()
	restrict = ()

	def get_object(self, resp, model_class, **kwargs):
		obj = super().get_object(resp, model_class, **kwargs)
		user = self.get_user(self.req)
		if user.get_role() == UserRole and obj.user_uuid != user.user_uuid:
			raise NoResultFound
		return obj


class PaymentList(List):
	scheme_class = PaymentSchemeGet
	model_class = model.Payment
	entity_plural = 'Payments'
	path_parameters = ()
	security = (DEFAULT_SECURITY)
	restrict = ()

	def modify_query_from_filtering_for_list(self, filtering, **kwargs):
		filt, ret = super().modify_query_from_filtering_for_list(filtering, **kwargs)
		user = self.get_user(self.req)
		if user.get_role() != AdminRole:
			cls = self.model_class
			ret = ret.filter(cls.user_uuid == user.user_uuid)
		return filt, ret


class PaypalWebhook(CustomPostAction):
	scheme_class = PaymentScheme
	model_class = model.Payment
	entity = 'Payment'
	path_parameters = ()
	security = (DEFAULT_SECURITY)
	restrict = ()

	no_auth_needed = True

	def on_post(self, req, resp, **kwargs):
		return self.proceed(req, resp, **kwargs)

	def proceed(self, req, resp, **kwargs):
		req_ip = get_request_ip(req)
		l = model.TransactionLog(transaction_src=req.data, from_ip=req_ip, type='paypal')
		try:
			conf = model.ConfigPayment.get(1)
			settings.PAYPAL['client_id'] = conf.paypal_pkey
			settings.PAYPAL['client_secret'] = conf.paypal_skey
			if conf.paypal_test_mode:
				settings.PAYPAL['mode'] = 'sandbox'
			else:
				settings.PAYPAL['mode'] = 'live'
			paypalrestsdk.configure(settings.PAYPAL)
		except Exception as e:
			l.result = 'bad paypal configuration:{}'.format(e)
			l.save()
			self.set_response(resp, OperationalError(e))
			return False
		try:
			log.debug('webhook called request data {} kwargs {}'.format(req.data, kwargs))
			data = req.data
			if 'event_type' in data:
				l.transaction_type = data['event_type']
				if data["event_type"] == 'PAYMENT.SALE.COMPLETED':
					pay_id = data['resource']['parent_payment']
					l.transaction_id = pay_id
					pay = paypalrestsdk.Payment.find(pay_id)
					# l.transaction_src = pay
					if 'transactions' in pay and pay['transactions']:
						tr = pay['transactions'][0]
						try:
							l.transaction_fee = float(tr['related_resources'][0]['sale']['transaction_fee']['value'])
						except:
							pass
						if 'amount' in tr and 'total' in tr['amount']:
							l.amount_total = tr['amount']['total']
						items = tr['item_list']['items']
						license_lrn = None
						license_switch = None
						for item in items:
							if 'LRN' in item['name'].upper():
								l.amount_lrn = float(item['price'])
								l.license_lrn_uuid = item['sku']
								license_lrn = model.LicenseLrn.get(l.license_lrn_uuid);
								lic = license_lrn
								if not license_lrn:
									raise Exception('wrong license lrn uuid - must be in "sku" field')
								if item['quantity'] != 1:
									raise Exception('wrong license lrn quantity - must be 1')
								hist = license_lrn.add_history('paypal')
								if hist:
									l.session().add(hist)
							if 'SWITCH' in item['name'].upper():
								l.amount_switch = float(item['price'])
								l.license_switch_uuid = item['sku']
								license_switch = model.LicenseSwitch.get(l.license_switch_uuid)
								lic = license_switch
								if not license_switch:
									raise Exception('wrong license switch uuid - must be in "sku" field')
								if item['quantity'] != 1:
									raise Exception('wrong license switch quantity - must be 1')
								hist = license_switch.add_history('paypal')
								if hist:
									l.session().add(hist)

						if l.license_lrn_uuid or l.license_switch_uuid:
							if license_lrn:
								u = license_lrn.user
								if license_switch:
									u1 = license_switch.user
									if u.user_uuid != u1.user_uuid:
										raise Exception(
											'LRN license and SWITCH licence from different users: {} and {}'.format(
												u.name, u1.name))
							else:
								u = license_switch.user
							pay = model.Payment(user_uuid=u.user_uuid,
												license_lrn_uuid=l.license_lrn_uuid,
												license_switch_uuid=l.license_switch_uuid,
												amount_lrn=l.amount_lrn,
												amount_switch=l.amount_switch,
												type='paypal',
												description=pay_id
												)
							pay_uuid = pay.save()
							l.payment_uuid = pay_uuid
							l.result = 'ok'
							l.status = 'success'
							l.save()
							ret = None
							if u.alert_payment_received:
								ret = pay.apply_mail('payment_received')
							if ret:
								l.result = 'ok, but email notification not sent: {}'.format(str(ret))
								l.save()

					else:
						l.result = 'paypal transaction error: empty transaction'
						l.status = 'fail'
					log.debug('pay {}'.format(pay))
					l.save()
				else:
					log.debug('---event {}'.format(data["event_type"]))
			else:
				l.result = 'paypal transaction error: wrong paypal event'
				l.save()
				self.set_response(resp, responses.ObjectNotFoundErrorResponse())
				return False
		except Exception as e:
			try:
				l.result = 'paypal transaction error:{}'.format(str(e))
				l.save()
				self.set_response(resp, OperationalError(e))
				return False
			except Exception as e1:
				from traceback import format_exc
				log.debug('paypal accept failure:{}'.format(format_exc()))
				l.session().rollback()
				self.set_response(resp, OperationalError(e1))
				return False
		return True


class StripeWebhook(CustomPostAction):
	scheme_class = PaymentScheme
	model_class = model.Payment
	entity = 'Payment'
	path_parameters = ()
	security = (DEFAULT_SECURITY)
	restrict = ()

	no_auth_needed = True

	def on_post(self, req, resp, **kwargs):
		return self.proceed(req, resp, **kwargs)

	def proceed(self, req, resp, **kwargs):
		req_ip = get_request_ip(req)
		l = model.TransactionLog(transaction_src=req.data, from_ip=req_ip, type='paypal')
		try:
			conf = model.ConfigPayment.get(1)
			stripe.api_key = conf.stripe_skey
			log.debug('webhook called request data {} kwargs {}'.format(req.data, kwargs))
		except Exception as e:
			l.result = 'bad stripe configuration:{}'.format(e)
			l.save()
			self.set_response(resp, OperationalError(e))
			return False
		data = req.data
		if "type" in data:
			l.transaction_type = data["type"]
			if data["type"] == 'charge.succeeded':
				try:
					charge_id = data['data']['object']['id']
					charge = stripe.Charge.retrieve(charge_id)
					l.transaction_id = charge_id
					l.transaction_src = charge
					description = charge['description']
					li = description.split(',')
					lrn_license_uuid = li[0]
					l.license_lrn_uuid = lrn_license_uuid
					switch_license = None
					switch_license_uuid = None
					if len(li) > 1:
						switch_license_uuid = li[1]
						switch_license = model.LicenseSwitch.get(switch_license_uuid)
						l.license_switch_uuid = switch_license_uuid

					lrn_license = model.LicenseLrn.get(lrn_license_uuid)
					amount_lrn = 0.0
					if not lrn_license:
						lrn_license_uuid = None
					else:
						amount_lrn = lrn_license.amount
						l.amount_lrn = amount_lrn
						hist = lrn_license.add_history('stripe')
						if hist:
							l.session().add(hist)
					amount_switch = 0.0
					if not switch_license:
						switch_license_uuid = None
					else:
						amount_switch = switch_license.amount
						l.amount_switch = amount_lrn
						hist = switch_license.add_history('stripe')
						if hist:
							l.session().add(hist)
					amount = charge['amount'] / 100
					l.amount_total = amount
					ucls = model.User
					u = ucls.filter(ucls.email == charge['source']['customer']).first()
					if not u and lrn_license:
						u = lrn_license.user
					if not u and switch_license:
						u = switch_license.user
					if u:
						if not lrn_license_uuid and not switch_license:
							u.total_amount = amount
							u.payment_type = 'stripe'
							u.apply_mail('payment_failed')
							return True
						if amount < amount_lrn + amount_switch:
							u.total_amount = amount
							u.payment_type = 'stripe'
							u.apply_mail('payment_failed')
							return True

						pay = model.Payment(user_uuid=u.user_uuid,
											license_lrn_uuid=lrn_license_uuid,
											license_switch_uuid=switch_license_uuid,
											amount_lrn=amount_lrn,
											amount_switch=amount_switch,
											type='stripe',
											description=charge_id
											)
						pay_uuid = pay.save()
						l.payment_uuid = pay_uuid
						l.result = 'ok'
						l.status = 'success'
						l.save()
						try:
							charge.update(dict(metadata=dict(payment_uuid=pay_uuid)))
						except:
							pass
						ret = None
						if u.alert_payment_received:
							ret = pay.apply_mail('payment_received')
						if ret:
							l.result = 'ok, but email notification not sent: {}'.format(str(ret))
							l.save()

				except Exception as e:
					l.result = 'stripe transaction error:{}'.format(str(e))
					l.save()
					self.set_response(resp, OperationalError(e))
					return False
			else:
				log.debug('---event {}'.format(data["type"]))
				l.result = 'paypal transaction error: wrong stripe event'
				l.save()
				self.set_response(resp, responses.ObjectNotFoundErrorResponse())
		else:
			l.result = 'paypal transaction error: wrong stripe data'
			l.save()
			self.set_response(resp, responses.ObjectNotFoundErrorResponse())
			return False
		return True


# Multi license create
class LicenseCreate(CustomPostAction):
	scheme_class = LicenseScheme
	scheme_class_get = LicenseResponseScheme
	model_class = model.LicenseLrn
	entity = 'LicenseLrn_LicenseSwitch'
	path_parameters = ()
	security = (DEFAULT_SECURITY)
	restrict = ()
	body_parameters = ('Create both LRN and swith licenses', scheme_class,)
	additional_responses = (SuccessResponseObjectInfo(payload_scheme=scheme_class_get),)

	def apply(self, obj, req, resp, **kwargs):
		license_lrn_uuid = None
		license_switch_uuid = None
		errors = self.scheme_class().validate(req.data)
		if errors:
			raise ValidationError(errors)
		user = self.get_user(req)
		obj = None
		if 'license_lrn' in req.data:
			req_data = req.data['license_lrn']
			scheme = LicenseLrnScheme().load(req_data)
			obj = scheme.data
			obj.user_uuid = user.user_uuid
			if not obj.start_time:
				obj.start_time = datetime.now(UTC)
			if obj.duration:
				obj.end_time = add_months(obj.start_time, obj.dur_months)
			license_lrn_uuid = obj.save()
		try:
			if 'license_switch' in req.data:
				req_data = req.data['license_switch']
				scheme = LicenseSwitchScheme().load(req_data)
				obj = scheme.data
				obj.user_uuid = user.user_uuid
				if not obj.start_time:
					obj.start_time = datetime.now(UTC)
				if obj.duration:
					obj.end_time = add_months(obj.start_time, obj.dur_months)
				license_switch_uuid = obj.save()
		except Exception as e:
			if license_lrn_uuid:
				model.LicenseLrn.get(license_lrn_uuid).delete()
			raise e
		if user and obj and user.alert_license_purchased:
			obj.apply_mail('license_purchased')
		data = dict(license_lrn_uuid=license_lrn_uuid, license_switch_uuid=license_switch_uuid)
		self.set_response(resp, SuccessResponseObjectInfo(payload_scheme=self.scheme_class_get, data=data))
		pass


# +++LicenseLrn+++
class LicenseLrnCreate(Create):
	scheme_class = LicenseLrnScheme
	model_class = model.LicenseLrn
	entity = 'LicenseLrn'
	path_parameters = ()
	security = (DEFAULT_SECURITY)
	restrict = ()

	def before_create(self, obj, **kwargs):
		user = self.get_user(self.req)
		obj.user_uuid = user.user_uuid
		cls = self.model_class
		# q = cls.filter(and_(cls.package_lrn_uuid == obj.package_lrn_uuid, cls.user_uuid == obj.user_uuid)).first()
		# if q:
		#     raise ValidationError({'package_lrn_uuid': ['duplicate package uuid {}'.format(obj.package_lrn_uuid)]})

		if not obj.start_time:
			obj.start_time = datetime.now(UTC)
		if obj.duration:
			obj.end_time = add_months(obj.start_time, obj.dur_months)

		return obj

	def after_create(self, object_id, req, resp, **kwargs):
		obj = self.model_class.get(object_id)
		if obj.user.alert_license_purchased:
			obj.apply_mail('license_purchased')


class LicenseLrnResource(Resource):
	model_class = model.LicenseLrn
	scheme_class = LicenseLrnScheme
	scheme_class_get = LicenseLrnSchemeGet
	scheme_class_modify = LicenseLrnSchemeModify
	entity = 'LicenseLrn'
	id_field = 'license_lrn_uuid'
	security = (DEFAULT_SECURITY)
	path_parameters = ()
	restrict = ()


class LicenseLrnRenewResource(CustomPatchAction):
	model_class = model.LicenseLrn
	scheme_class = LicenseLrnSchemeGet
	entity = 'LicenseLrn'
	id_field = 'license_lrn_uuid'
	security = (DEFAULT_SECURITY)
	path_parameters = ({'name': 'license_lrn_uuid'},)
	restrict = ()
	body_parameters = ()

	def apply(self, obj, req, resp, **kwargs):
		lic = self.model_class.get(kwargs['license_lrn_uuid'])
		if not lic:
			raise ValidationError({'license_lrn_uuid': ['license_lrn_uuid not found']})
		obj.renew()
		obj.save()
		self.scheme_class.get_object_created_response()
		data = self.get_object_data(resp, self.model_class, self.scheme_class, **kwargs)
		if data:
			self.set_response(resp, responses.SuccessResponseObjectInfo(data=data))
			return False
		return True


class LicenseLrnList(List):
	scheme_class = LicenseLrnSchemeGet
	model_class = model.LicenseLrn
	entity_plural = 'LicenseLrns'
	path_parameters = ()
	security = (DEFAULT_SECURITY)
	restrict = ()

	def modify_query_from_filtering_for_list(self, filtering, **kwargs):
		filt, ret = super().modify_query_from_filtering_for_list(filtering, **kwargs)
		user = self.get_user(self.req)
		if not user.is_admin:
			cls = self.model_class
			ret = ret.filter(cls.user_uuid == user.user_uuid)
		return filt, ret


# ---LicenseLrn---

# +++LicenseSwitch+++
class LicenseSwitchCreate(Create):
	scheme_class = LicenseSwitchScheme
	model_class = model.LicenseSwitch
	entity = 'LicenseSwitch'
	path_parameters = ()
	security = (DEFAULT_SECURITY)
	restrict = ()

	def before_create(self, obj, **kwargs):
		user = self.get_user(self.req)
		obj.user_uuid = user.user_uuid
		# obj.created_by=user.name
		cls = self.model_class
		# q = cls.filter(and_(cls.package_switch_uuid == obj.package_switch_uuid, cls.user_uuid == obj.user_uuid)).first()
		# if q:
		#     raise ValidationError(
		#         {'package_switch_uuid': ['duplicate package uuid {}'.format(obj.package_switch_uuid)]})
		if not obj.start_time:
			obj.start_time = datetime.now(UTC)
		if obj.duration:
			obj.end_time = add_months(obj.start_time, obj.dur_months)
		mcls = model.DnlLicenseInfo
		if obj.switch_uuid:
			q = mcls.filter(and_(mcls.uuid == obj.switch_uuid, mcls.recv_ip == obj.ip)).first()
			if not q:
				raise ValidationError({'package_switch_uuid': ['no such switch and ip']})
		return obj

	def after_create(self, object_id, req, resp, **kwargs):
		obj = self.model_class.get(object_id)
		if obj.user.alert_license_purchased:
			obj.apply_mail('license_purchased')


class LicenseSwitchResource(Resource):
	model_class = model.LicenseSwitch
	scheme_class = LicenseSwitchScheme
	scheme_class_get = LicenseSwitchSchemeGet
	scheme_class_modify = LicenseSwitchSchemeModify
	entity = 'LicenseSwitch'
	id_field = 'license_switch_uuid'
	security = (DEFAULT_SECURITY)
	path_parameters = ()
	restrict = ()


class LicenseSwitchRenewResource(CustomPatchAction):
	model_class = model.LicenseSwitch
	scheme_class = LicenseSwitchSchemeGet
	entity = 'LicenseSwitch'
	id_field = 'license_switch_uuid'
	security = (DEFAULT_SECURITY)
	path_parameters = ({'name': 'license_switch_uuid'},)
	restrict = ()

	def apply(self, obj, req, resp, **kwargs):
		lic = self.model_class.get(kwargs['license_switch_uuid'])
		if not lic:
			raise ValidationError({'license_switch_uuid': ['license_switch_uuid not found']})
		obj.renew()
		obj.save()
		self.scheme_class.get_object_created_response()
		data = self.get_object_data(resp, self.model_class, self.scheme_class, **kwargs)
		if data:
			self.set_response(resp, responses.SuccessResponseObjectInfo(data=data))
			return False
		return True


class LicenseSwitchList(List):
	scheme_class = LicenseSwitchSchemeGet
	model_class = model.LicenseSwitch
	entity_plural = 'LicenseSwitchs'
	path_parameters = ()
	security = (DEFAULT_SECURITY)
	restrict = ()

	def modify_query_from_filtering_for_list(self, filtering, **kwargs):
		filt, ret = super().modify_query_from_filtering_for_list(filtering, **kwargs)
		user = self.get_user(self.req)
		if not user.is_admin:
			cls = self.model_class
			ret = ret.filter(cls.user_uuid == user.user_uuid)
		return filt, ret

# ---LicenseSwitch---
