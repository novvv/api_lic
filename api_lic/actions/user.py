import json
from falcon_rest.signals import receive
#from falcon_rest.contrib.auth.auth_signals import auth_success, auth_failed
from ..auth.auth_signals import auth_success, auth_failed
#from falcon_rest.contrib.middleware.middleware_signals import process_resource_end,process_request_start
from ..middleware.middleware_signals import process_resource_end,process_request_start
from falcon_rest.db import orm
from falcon_rest.helpers import get_request_ip
from falcon_rest.conf import settings
from falcon_rest.logger import log

#from .. model import AuthorizationLog,WebSession

@receive(process_request_start, send_sender=False, send_keys=['req', 'resp'])
def on_process_request_start(req,resp):
    if hasattr(settings,'ALLOW_ORIGIN') and  ( '*' in settings.ALLOW_ORIGIN or req.headers.get('ORIGIN') in settings.ALLOW_ORIGIN ):
            if 'ORIGIN' in req.headers:
                resp.append_header('Access-Control-Allow-Origin', req.headers['ORIGIN'])
                resp.append_header('Access-Control-Allow-Headers', 'Authorization, Content-Type, X-Auth-Token,Cache-Control,X-Requested-With')
                resp.append_header('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE')
                log.debug('CORS headers to {}'.format(req.headers.get('ORIGIN')))
            else:
                log.debug('CORS headers not send: no ORIGIN')
    else:
        log.debug('CORS headers not send: not ALLOW')

def check_req(req):
    return req.context['app_name'] == 'lic_api'
@receive(auth_success, send_sender=False, send_keys=['req', 'user'])
def on_auth_success(req, user):

    if not check_req(req):
        return

    user.last_login_time = orm.func.now()
    #user.login_ip = get_request_ip(req)
    #user.is_online = 1
    user.save()

    #from ..model import AuthorizationLog, WebSession
    #WebSession(user_id=user.user_id,host=get_request_ip(req),agent=req.user_agent,msg=json.dumps(dict(succes=True))).save()
    #AuthorizationLog(username=user.name,request_ip=user.login_ip,direction=req.method,auth_type='pass',error_type='success').set_time().save()

@receive(auth_failed, send_sender=False, send_keys=['req', 'data'])
def on_auth_failed(req, data):
    if not check_req(req):
        return
    #from ..model import AuthorizationLog, WebSession
    #WebSession(user_id=None,host=get_request_ip(req),agent=req.user_agent,msg=json.dumps(dict(success=False,email_or_name=data['email_or_name'],password=data['password']))
    #).save()
    #AuthorizationLog(username=data['email_or_name'], request_ip=get_request_ip(req),
    #        entered_password=data['password'],direction=req.method,
    #        auth_type='pass', error_type='fail').set_time().save()

@receive(process_resource_end, send_sender=False, send_keys=['req'])
def on_process_resource_end(req):
    if not check_req(req):
        return

    try:
        req.context['user'].last_login = orm.func.now()
        #req.context['user'].is_online = 0
        req.context['user'].save()
    except KeyError:  # if no user were set
        pass
