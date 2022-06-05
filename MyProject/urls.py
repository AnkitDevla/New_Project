from django.contrib import admin
from django.urls import include, path
from MyApp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('trainerdata/',include('CURD_api.urls')),
    path('traineedata/',include('CURD_api.urls')),
    path('doubtsdata/',include('CURD_api.urls')),
]
