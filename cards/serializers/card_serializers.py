from rest_framework import serializers

from cards.models.main_deck_card import MainDeckCard


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainDeckCard
        fields = ("card_name", "card_text")
