from falcon_rest.contrib.rbac import (
    RbacAcl, RbacPermAllow as Allow, RbacPermDeny as Deny, RbacRoleNoRole
)

from api_lic.views.user import UserInfoResource, UserResetPasswordEmail
from falcon_rest.responses import UnauthenticatedErrorResponse,ForbiddenErrorResponse
from . rbac_role import AdminRole, CompanyAdminRole,UserRole
from .. views import *
acl = RbacAcl(
    default_perm=Deny,
    security_conf=((AdminRole, 'auth_token'), (UserRole, 'auth_token'), (CompanyAdminRole, 'auth_token')),
    additional_responses_conf=(
        dict(forbidden=RbacRoleNoRole, responses=(UnauthenticatedErrorResponse, )),
        dict(allow=AdminRole, forbidden=UserRole, responses=(ForbiddenErrorResponse, )),
    )
)
#acl.add_rule_multiple(resources=(file.UploadFile, ), roles=(RbacRoleNoRole, Member, Admin), perm=Allow)
#acl.add_rule_multiple(resources=(file.GetDownloadLink, ), roles=(Member, Admin), perm=Allow)
#acl.add_rule_multiple(resources=(file.ShowFile, ), roles=(RbacRoleNoRole, Member, Admin), perm=Allow)
#acl.add_rule(resource=file.ListTmpFiles, role=Admin, perm=Allow)
#acl.add_rule(resource=file.ListFiles, role=Admin, perm=Allow)
#acl.add_rule(resource=signup_info.Resource, role=Admin, perm=Allow)
#acl.add_rule(resource=signup_info.List, role=Admin, perm=Allow)

#public
acl.add_rule_multiple(resources=(UserRegisterCreate, UserResetPassword, UserConfirmRegister), roles=(RbacRoleNoRole,), perm=Allow)
# auth
acl.add_rule_multiple(resources=(UserCreate,UserResource,UserList,UserByEmailResource),roles=(AdminRole,),perm=Allow)

acl.add_rule_multiple(resources=(UserInfoResource,UserResetPasswordEmail,UserResetPassword),methods=('get','patch'),roles=(UserRole,CompanyAdminRole,AdminRole),perm=Allow)
acl.add_rule_multiple(resources=(ObjectRevisionList,),roles=(AdminRole,UserRole),perm=Allow)

#admin
acl.add_rule_multiple(resources=(EmailTemplateResource, EmailTemplateList,PlanCreate,PlanResource,NotificationCreate,NotificationResource),
                      roles=(AdminRole,),perm=Allow)
acl.add_rule_multiple(resources=(PackageSwitchCreate,PackageSwitchResource,PackageLrnCreate,PackageLrnResource),
                      roles=(AdminRole,),perm=Allow)
acl.add_rule_multiple(resources=(ConfigPaymentResource,),
                      roles=(AdminRole,),perm=Allow)
#user
acl.add_rule_multiple(resources=(PaymentCreate,PaymentResource),roles=(UserRole,),perm=Allow)

#admin&user
acl.add_rule_multiple(resources=(PackageSwitchList,PackageLrnList,NotificationList,PaymentList),roles=(AdminRole,UserRole),perm=Allow)
