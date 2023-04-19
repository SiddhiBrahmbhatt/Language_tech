from rest_framework.serializers import ModelSerializer
from translate import Translator
from typing import Dict

from .models import Translate


class TranslateSerializer(ModelSerializer):
    """
    Serializer for the Translate model.

    Attributes:
        from_language: A string representing the source language.
        text: A string representing the text to be translated.
        to_language: A string representing the target language.
        translation: A string representing the translated text.
    """

    class Meta:
        """
        Defines the metadata for the serializer.
        """
        model = Translate
        fields = ['from_language', 'text', 'to_language', 'translation']

    def create(self, validated_data: Dict) -> Translate:
        """
        Creates a new Translate instance using validated data.

        Args:
            validated_data: A dictionary containing validated data for the Translate instance.

        Returns:
            The created Translate instance.
        """
        from_language = validated_data.get('from_language')
        to_language = validated_data.get('to_language')
        text = validated_data.get('text')
        translator = Translator(from_lang=from_language, to_lang=to_language)
        translation = translator.translate(text)
        translate = Translate.objects.create(
            from_language=from_language,
            to_language=to_language,
            text=text,
            translation=translation
        )
        return translate
