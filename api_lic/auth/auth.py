from datetime import datetime, timedelta
import bcrypt
import jwt
from falcon_rest.conf import settings

def get_hashed_password(plain_text_password):
    if not plain_text_password:
        import random
        plain_text_password=str(round(random.random()*1000000000,0))
    if isinstance(plain_text_password,type('')):
        plain_text_password=plain_text_password.encode()
    hash=bcrypt.hashpw(
        plain_text_password,
        bcrypt.gensalt()
    )
    if isinstance(hash,type(b'')):
        hash=hash.decode()
    return hash


def check_password(plain_text_password, hashed_password):
    try:
        return bcrypt.checkpw(
            plain_text_password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )
    except ValueError:  # pragma: no cover
        return False


def get_token(user, ttl=None):
    token_data = user.get_token_data()
    valid_till = datetime.now() + timedelta(
        hours=ttl if ttl else settings.JWT_TTL_DAYS)
    token_data['exp'] = int(valid_till.timestamp())

    token = jwt.encode(token_data, settings.JWT_SIGNATURE, algorithm='HS256')
    if hasattr(user, 'on_token_created'):
        user.on_token_created(token_data.get('jti'), token, valid_till)
    return token.decode('utf-8')


def get_user_from_token(token):
    try:
        token_data = jwt.decode(token, settings.JWT_SIGNATURE)
        return settings.get_auth_user_model(
            role=token_data.get('role')).get_user_from_token_data(token_data)
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return None


def decode_without_verification(token):
    return jwt.decode(token, settings.JWT_SIGNATURE, verify=False)

def get_token_exp(token):
    data = decode_without_verification(token)
    exp = data.get('exp',None)
    if exp:
        return datetime.utcfromtimestamp(exp)
    return None