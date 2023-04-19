from typing import List
from rest_framework import generics

from .models import Translate
from .serializers import TranslateSerializer


class TranslateView(generics.ListCreateAPIView):
    """
    Defines a class-based view for creating and listing instances of the Translate model.

    Inherits from ListCreateAPIView from the Django REST framework.
    Expects a GET request to list all instances of Translate and a POST request
    to create a new instance of Translate.

    Attributes:
        queryset: A QuerySet containing all instances of the Translate model.
        serializer_class: A Serializer class to handle translation data.
    """
    queryset: List[Translate] = Translate.objects.all()
    serializer_class: TranslateSerializer = TranslateSerializer
