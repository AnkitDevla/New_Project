from django.urls import path, include
from doubt.models import Doubts
from . import views
from doubt.views import Trainer,Trainee,Doubts


urlpatterns = [
        path('trainers/', views.trainer_post),
        path('trainers/<int:id>/',  views.trainer),
        path('trainees/', views.trainee_post),
        path('trainees/<int:id>/',  views.trainee),
        path('doubts/', views.doubt_post),
        path('doubts/<int:id>/',  views.doubt),
]
