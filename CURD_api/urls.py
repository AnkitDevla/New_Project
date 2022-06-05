from django.urls import path, include

from CURD_api.models import Doubts
from . import views
from .views import Trainer,Trainee,Doubts


urlpatterns = [
    path('trainer/',views.trainerapi),
    path('trainee/',views.traineeapi),
    path('doubts/',views.doubtsapi)
]
