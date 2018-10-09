import cli_lic
from datetime import datetime,timedelta
from pytz import UTC
import json
import pprint
#cli_lic.configuration.host='http://158.69.221.111/api_lic/v1'
#cli_lic.configuration.host='http://localhost:8002/v1'
admin_token=None
tokens={}
from api_lic.settings import JWT_SIGNATURE,ADMIN_UUID,TEST_USER_UUID
def auth(user_id=ADMIN_UUID):
    global admin_token
    # if not user_id:
    #     if not admin_token:
    #         api=cli_lic.apis.AuthApi()
    #         r=api.auth_post(body={'user_name':'admin','password':'yoo5Iche'})
    #         admin_token=r.payload.token
    #     cli_lic.configuration.api_key['X-Auth-Token'] = admin_token

    import jwt
    data=dict(user_uuid=user_id,exp=int((datetime.now(UTC) + timedelta(hours=1)).timestamp()))
    cli_lic.configuration.api_key['X-Auth-Token']=jwt.encode(data, JWT_SIGNATURE, algorithm='HS256').decode('utf-8')
    print(user_id,cli_lic.configuration.api_key['X-Auth-Token'])

def auth_user(user_id=TEST_USER_UUID):
    return auth(user_id=user_id)

def logoff():
    cli_lic.configuration.api_key['X-Auth-Token'] = None

def auth_random(**kwargs):
    auth()
    mems = cli_lic.AuthApi().user_list_get(**kwargs)
    items = mems.payload.items
    if len(items):
        random.shuffle(items)
        auth(items[0].user_id)
        return items[0]
    print('not found!')


import random 
def bla(l=24,digits=False):
    if digits:
        letters=[chr(i) for i in range(48,58)]+[chr(i) for i in range(65,91)]
    else:
        letters=[chr(i) for i in range(97,123)]
    ret=''
    for c in range(0,l):
        ret=ret+random.choice(letters)
    return ret.capitalize()

def bla_bla(l):
    ret = bla(random.randint(1,5))
    for i in range(0,l):
        ret += bla(random.randint(1,10)).lower()
        if random.randint(0, 7) == 0:
            ret += bla(random.randint(2,7)).lower()+' '
        if (i % 7 )==0:
            ret += '. '+bla(random.randint(4,7))
        else:
            if  random.randint(0,14) == 0:
                ret +=', '
            else:
                ret +=' '
    return ret

def dig(l=12):
    letters=[chr(i) for i in range(48,58)]
    ret=''
    for c in range(0,l):
        ret=ret+random.choice(letters)
    return ret

def ip():
    l=[]
    for i in range(0,4):
        l.append(str(random.randint(0,255)))
    return '.'.join(l)
def bla_mail(set=0):
    if set==1:
        #return 'mizdesino@gmail.com'
        return 'testuser@denovolab.com'
    if set==2:
        return 'novvvster@gmail.com'
    if set==3:
        return '_novvv@mail.ru'
    return bla(5)+'.'+bla(4)+'@'+bla(5)+'.'+bla(4)+'.'+random.choice(['com','com','net','org','cc','us','eu'])
def bla_comp():
    return bla(random.randint(0,6))+' '+bla(random.randint(0,6))+' ' +random.choice(['inc.','ltd.','&K','broth'])

def lorem_ipsum():
    return bla(6)+' '+ bla(2)+' '+ bla(4)+', '+bla(6)+' '+ bla(2)+' '+ bla(5)+' '+ bla(4)+' '+ bla(7)+'. ' +""" Lorem ipsum
 dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
 Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
 Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

def bla_bool():
    return random.choice([True,False])

def bla_url():
    return 'http://{}.{}/index.html'.format(bla(8).lower(), random.choice(['com', 'org', 'ru', 'us']))

def bla_contact(**kwargs):
    data = dict(
    first_name=bla(10),
    last_name = bla(10),
    email = bla_mail(),
    phone = dig(10),
    address = bla_bla(3),
    city = bla(random.randint(3,10)),
    state = bla(2),
    zipcode = dig(6),
    country_uuid = random.choice(['1','1-','7','49']),
    passwd = bla(10),
    )
    for k,v in kwargs.items():
        data[k]=v
    return data

def rand_rate(**kwargs):
    ret = cli_lic.PublicApi().rate_list_get(**kwargs)
    assert (ret.success and len(ret.payload.items))
    it = random.choice(ret.payload.items)
    return (it.rate_uuid,it,ret.payload.items)