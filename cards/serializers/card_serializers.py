from rest_framework import serializers

from cards.models.amazon_brand_model import GVBrand


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GVBrand
        fields = ("brand_registry_name", "brand_entity_id")
