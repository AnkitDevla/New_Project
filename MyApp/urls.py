from django.urls import path, include
from . import views
from .views import Trainer,Trainee


urlpatterns = [
    path('trainer/',views.trainerapi)
]
