from django.contrib import admin
from django.urls import include, path
from doubt import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('doubt.urls')),
]

