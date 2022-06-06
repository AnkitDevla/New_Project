from django.urls import path, include
from doubts.models import Doubts
from . import views
from doubts.views import Trainer,Trainee,Doubts


urlpatterns = [
    path('trainers/<int:id>/',  views.Trainer),
    path('trainees/<int:id>/',  views.Trainee),
    path('doubts/<int:id>/',  views.Doubts),
]
