from django.urls import path

from .views import card

urlpatterns = [
    path("cards", card.index, name="card-list"),
]