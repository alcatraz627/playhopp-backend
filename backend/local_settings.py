########################################
###########  Custom settings ###########
########################################
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'pwdplayhopp',
        'HOST': 'database-1.cnmqi18xci2d.ap-south-1.rds.amazonaws.com',
        'PORT': '5432'
    }
}

# https://chrisbartos.com/articles/how-to-implement-token-authentication-with-django-rest-framework/
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

# AUTHENTICATION_BACKENDS = ['customers.user_backend.EmailBackend']
# ADMIN_LOGIN = 'email'

AUTH_USER_MODEL = 'customers.Customer'

ALLOWED_HOSTS = ['ec2-35-154-205-76.ap-south-1.compute.amazonaws.com', '35.154.205.76', 'localhost', '0.0.0.0']
