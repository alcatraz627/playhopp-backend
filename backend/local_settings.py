########################################
###########  Custom settings ###########
########################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'playhopp',
        'USER': 'playhopp',
        'PASSWORD': 'pwdplayhopp',
        'HOST': 'localhost',
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
