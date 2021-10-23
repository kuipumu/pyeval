"""
Base App Config.
https://docs.djangoproject.com/en/3.2/ref/applications/
"""

from django.apps import AppConfig

app_name = 'base'

class BaseConfig(AppConfig):
    """
    App configuration.
    """
    # Set app default auto field.
    # https://docs.djangoproject.com/en/3.2/ref/applications/#django.apps.AppConfig.default_auto_field
    default_auto_field = 'django.db.models.BigAutoField'
    # Set app name.
    # https://docs.djangoproject.com/en/3.2/ref/applications/#django.apps.AppConfig.name
    name = 'base'
