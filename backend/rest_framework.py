#Rest Frameowrk Authentication Configuration for JWT Token Authentication 
from datetime import timedelta


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    "SILDING_TOKEN_LIFETIME": timedelta(days=1),
}