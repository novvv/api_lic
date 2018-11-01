from .user import UserConfirmRegister, UserForgotPassword, UserResetPassword, NotificationList, PaymentCreate, \
    PaymentResource, PaymentList, PaypalWebhook, StripeWebhook,LicenseLrnCreate,LicenseLrnResource,LicenseLrnRenewResource,LicenseLrnList,\
    LicenseSwitchCreate,LicenseSwitchResource,LicenseSwitchList
from .public import SimpleFileCreate, SimpleFileGet
from .admin import EmailTemplateResource, EmailTemplateList, PlanCreate, PlanResource, NotificationCreate, \
    NotificationResource,PackageLrnCreate,PackageLrnResource,PackageLrnList,PackageSwitchCreate,PackageSwitchResource,\
    PackageSwitchList,SwitchCreate,SwitchResource,SwitchList,LicenseSwitchAdminResource,LicenseLrnAdminResource
