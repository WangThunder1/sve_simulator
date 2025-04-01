from django.db import models
from cards.models.base import CreatedOnMixin, UpdatedOnMixin

class MainDeckCard(models.Model):
    NEUTRAL:str ="Neutral"
    FORESTCRAFT:str ="Forestcraft"
    SWORDCRAFT:str ="Swordcraft"
    RUNECRAFT:str ="Runecraft"
    DRAGONCRAFT:str ="Dragoncraft"
    ABYSSCRAFT:str ="Abysscraft"
    HAVENCRAFT:str ="Havencraft"
    FOLLOWER:str ="Follower"
    AMULET:str ="Amulet"
    SPELL:str ="Spell"

    CRAFT_CHOICES = [
        (NEUTRAL, "Neutral"),
        (FORESTCRAFT, "Forestcraft"),
        (SWORDCRAFT, "Swordcraft"),
        (RUNECRAFT, "Runecraft"),
        (DRAGONCRAFT, "Dragoncraft"),
        (ABYSSCRAFT, "Abysscraft"),
        (HAVENCRAFT, "Havencraft"),
    ]
    TYPE_CHOICES = [
        (FOLLOWER, "Follower"),
        (AMULET, "Amulet"),
        (SPELL, "Spell"),
    ]

    card_cost = models.IntegerField(default=0)
    card_class = models.CharField(choices=CRAFT_CHOICES, default=NEUTRAL, max_length=18, help_text="Craft" ) # craft
    card_name = models.CharField(null=True, blank=True, max_length=128)
    card_text = models.TextField(null=True, blank=True)
    card_type = models.CharField(choices=TYPE_CHOICES, default=FOLLOWER, max_length=18)
    card_traits = models.JSONField(default=list, blank=True)# machina, etc
    set_number = models.CharField(null=False, blank=False, max_length=18, default='BP01-001EN')
    card_attack = models.IntegerField(default=0)
    card_defence = models.IntegerField(default=0)
    #set FK
    
    class Meta:
        app_label = 'cards'

