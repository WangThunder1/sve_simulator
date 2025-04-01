
from cards.serializers.card_serializers import CardSerializer

from django.http import HttpResponse
from rest_framework.views import APIView



class CardData(APIView):
    serializer_class = CardSerializer