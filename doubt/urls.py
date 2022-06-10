from django.urls import include, path
from . import views
# from doubt.views import trainer_api,trainee_api,doubts_api
from rest_framework.routers import DefaultRouter
# from doubt.views import TrainerViewSet, TraineeViewSet, DoubtsViewSet


urlpatterns = [
    path('trainers/', views.TrainersListCreate.as_view()),
    path('trainers/<int:pk>/',  views.TrainerRetrieveUpdateDestroy.as_view()),
    path('trainees/', views.TraineeListCreate.as_view()),
    path('trainees/<int:pk>/',  views.TraineeRetrieveUpdateDestroy.as_view()),
    path('doubts/', views.DoubtsListCreate.as_view()),
    path('doubts/<int:pk>/',  views.DoubtsRetrieveUpdateDestroy.as_view()),

    # viewset
    #     path('trainers/',.TrainerViewSet),





    # generic view urls

    #     path('trainers/', trainer_api.as_view()),
    #     path('trainees/', trainee_api.as_view()),
    #     path('doubts/', doubts_api.as_view()),



    # function based Api_view
    #     path('trainers/', views.trainer_post),
    #     path('trainers/<int:id>/',  views.trainer),
    #     path('trainees/', views.trainee_post),
    #     path('trainees/<int:id>/',  views.trainee),
    #     path('doubts/<int:id>/',  views.doubt),
    #     path('doubts/', views.doubt_post),
]
