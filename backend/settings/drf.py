REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# swagger docs
SPECTACULAR_SETTINGS = {
    'TITLE': 'Fix a Time',  # noqa
    'DESCRIPTION': 'Meeting creation app',
    'VERSION': '1.0.0',
    # OTHER SETTINGS
}
