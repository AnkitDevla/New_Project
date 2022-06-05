from .models import Trainer,Trainee 
from rest_framework import serializers


class TrainerSerializer(serializers.Serializer):
    class Meta:
        model = Trainer
        fields = ['name', 'age', 'email', 'contact_no','gender']


class TraineeSerializer(serializers.Serializer):
    class Meta:
        model = Trainee
        fields = ['name', 'age', 'email', 'contact_no','exp']