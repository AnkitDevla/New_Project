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

class DoubtsSerializer(serializers.Serializer):
    name = serializers.CharField()
    question = serializers.CharField()
    answer = serializers.CharField()
    question_from = serializers.StringRelatedField()
    answer_by = serializers.StringRelatedField()
    when_asked = serializers.DateTimeField()
    status = serializers.CharField()
