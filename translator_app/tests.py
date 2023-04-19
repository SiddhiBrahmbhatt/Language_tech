from django.test import TestCase
from translator_app.models import Translate


class TranslateModelTestCase(TestCase):
    """Test cases for the Translate model."""

    def setUp(self):
        self.translate = Translate.objects.create(
            from_language='EN',
            text='Hello, how are you?',
            to_language='ES',
            translation='Hola, ¿cómo estás?'
        )

    def test_translate_str_method(self):
        """Test the __str__ method of the Translate model."""
        self.assertEqual(
            str(self.translate),
            f'{self.translate.from_language} to {self.translate.to_language}'
        )

    def test_translate_model_fields(self):
        """Test the fields of the Translate model."""
        self.assertEqual(self.translate.from_language, 'EN')
        self.assertEqual(self.translate.text, 'Hello, how are you?')
        self.assertEqual(self.translate.to_language, 'ES')
        self.assertEqual(self.translate.translation, 'Hola, ¿cómo estás?')
