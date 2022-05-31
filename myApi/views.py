from rest_framework import viewsets

from .serializers import TrainerSerializer,TraineeSerializer
from .models import Trainer,Trainee


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all().order_by('name')
    serializer_class = TrainerSerializer

    

class TraineeViewSet(viewsets.ModelViewSet):
    queryset = Trainee.objects.all().order_by('name')
    serializer_class = TraineeSerializer

    