from django.contrib import admin
from django.urls import path,include
from django.urls import include, path
from rest_framework import routers
from myApi import views


router = routers.DefaultRouter()
router.register(r'Trainers', views.TrainerViewSet)
router.register(r'Trainees', views.TraineeViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("MyApp.urls")),
    path('myApi/', include('myApi.urls')),
]
