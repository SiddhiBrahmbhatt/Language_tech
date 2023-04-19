from django.db import models
from django.utils.translation import gettext as _


class LanguageChoices(models.TextChoices):
    EN = 'EN', _('English')
    FR = 'FR', _('French')
    ES = 'ES', _('Spanish')
    ZH = 'ZH', _('Chinese')


class Translate(models.Model):
    """
    A model to store translation details.

    Attributes:
        from_language: A CharField for the source language, limited to 500 characters.
        text: A TextField for the text to be translated.
        to_language: A CharField for the target language, limited to 500 characters.
        translation: A TextField for the translated text, nullable and not editable.
    """

    from_language = models.CharField(max_length=500, choices=LanguageChoices.choices, help_text=_('Enter the source language.'))
    text = models.TextField(help_text=_('Enter the text to be translated.'))
    to_language = models.CharField(max_length=500, choices=LanguageChoices.choices, help_text=_('Enter the target language.'))
    translation = models.TextField(null=True, blank=True, editable=False, help_text=_('The translated text.'))

    def __str__(self):
        return f'{self.from_language} to {self.to_language}'
