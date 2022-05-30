from django.contrib import admin
from .models import Trainee, Trainer

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_Trainer = ['name','age','email','contact_no','gender']

@admin.register(Trainee)    
class TraineeAdmin(admin.ModelAdmin):
    list_Trainee = ['name','age','email','contact_no','exp']