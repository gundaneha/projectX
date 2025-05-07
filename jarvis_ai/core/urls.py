from django.urls import path
from core import views  # Make sure to import views from the 'core' app

urlpatterns = [
    path("", views.index, name="index"),  # Home page
    path("ask/", views.ask, name="ask"),   # JARVIS AI endpoint (added trailing slash for consistency)
]