import jwt
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from .custom_user import CustomUser

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None

        try:
            access_token = auth_header.split(' ')[1]
            payload = jwt.decode(
                access_token, 
                settings.JWT_SECRET_KEY, 
                algorithms=['HS256']
            )
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Access token expired')
        except IndexError:
            raise AuthenticationFailed('Token prefix missing')
        except jwt.DecodeError:
            raise AuthenticationFailed('Invalid token')

        user = CustomUser(
            user_id=payload['user_id'],
            mobile_number=payload['mobile_number'],
            email=payload['email'],
            roles=payload['roles'],
            authenticated=True
        )
        return (user, None)