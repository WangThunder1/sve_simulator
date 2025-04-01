from django.contrib import admin
from cards.models.main_deck_card import MainDeckCard
# Register your models here.

@admin.register(MainDeckCard)
class MainDeckCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'card_name', 'card_class', 'card_type', 'set_number')
