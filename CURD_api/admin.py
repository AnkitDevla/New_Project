from django.contrib import admin
from .models import Trainee, Trainer,Doubts

# admin.site.register(Trainer)
# admin.site.register(Trainee)


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_Trainer = ['name','age','email','contact_no','gender']

@admin.register(Trainee)    
class TraineeAdmin(admin.ModelAdmin):
    list_Trainee = ['name','age','email','contact_no','exp']


@admin.register(Doubts)
class TraineeAdmin(admin.ModelAdmin):
    list_Trainee = ['name','question','answer','question_from','answer_by','when_asked','status']


