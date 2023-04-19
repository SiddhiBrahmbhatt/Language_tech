from django.apps import AppConfig


class TranslatorAppConfig(AppConfig):
    """
    Configuration class for the translator_app.

    Attributes:
        default_auto_field: The name of the field to use for automatically created AutoField's.
        name: The full Python path to the application.
    """
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'translator_app'
