from django.contrib import admin
from django.contrib.auth.models import Group
from translator_app.models import Translate


admin.site.unregister(Group)
admin.site.site_header: str = "Translator"


@admin.register(Translate)
class TranslateAdmin(admin.ModelAdmin):
    """
    ModelAdmin class for the Translate model in the Django admin site.

    Attributes:
        list_display: The fields to display in the model's list view.
        list_filter: The fields to use for filtering the model's records.
        search_fields: The fields to use for searching the model's records.
    """
    list_display: tuple = ['from_language', 'to_language']
    list_filter: tuple = ['from_language', 'to_language']
    search_fields: tuple = ['from_language', 'to_language']
