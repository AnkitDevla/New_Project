from django.shortcuts import render
from doubt.serializer import TrainerSerializer,TraineeSerializer,DoubtsSerializer
from doubt.models import Trainer,Trainee,Doubts
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status



@api_view(['GET', 'PUT', 'DELETE'])
def trainer(request, id):
    trainer = get_object_or_404(Trainer, pk=id)

    if request.method == 'GET':
        serializer = TrainerSerializer(trainer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TrainerSerializer(trainer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        trainer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def trainer_post(request):
    serializer = TrainerSerializer(trainer, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view(['GET', 'PUT', 'DELETE'])
def trainee(request, id):
    trainee = get_object_or_404(Trainee, pk=id)

    if request.method == 'GET':
        serializer = TraineeSerializer(trainee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TraineeSerializer(trainee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        trainee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def trainee_post(request):
    serializer = TraineeSerializer(trainee, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)