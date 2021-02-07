from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path("", views.index, name="search"),
    path("credits", views.credits, name="credits"),
    path("about", views.about, name="about")
]
