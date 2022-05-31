from rest_framework import serializers

from .models import Trainer,Trainee

class TrainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainer
        fields = ('name', 'age','email','contact_no','gender')

class TraineeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainee
        fields = ('name', 'age','email','contact_no','exp')