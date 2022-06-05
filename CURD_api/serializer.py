from .models import Trainer,Trainee,Doubts
from rest_framework import serializers


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['name', 'age', 'email', 'contact_no','gender']


class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = ['name', 'age', 'email', 'contact_no','exp']


class DoubtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doubts
        fields = ['name', 'question', 'answer', 'question_from','answer_by','when_asked','status']