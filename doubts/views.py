# from django.shortcuts import render
from doubts.serializer import TrainerSerializer,TraineeSerializer,DoubtsSerializer
from MyApp.models import Trainer,Trainee,Doubts
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET', 'PUT','POST', 'DELETE'])
def trainerapi(request,id):
    if request.method == "GET":
        trainers = Trainer.objects.all()
        serializer = TrainerSerializer(trainers,many=True)
        return Response(serializer.data)
    elif request.method =='PUT':
        trainers = Trainer.objects.all()
        serializer = TrainerSerializer(trainers,many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        trainers = Trainer.objects.all()
        serializer = TrainerSerializer(trainers,many=True)
        return Response(serializer.data)
    elif request.method =='DELETE':
        trainers = Trainer.objects.all()
        serializer = TrainerSerializer(trainers,many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT','POST', 'DELETE'])
def traineeapi(request):
    if request.method == "GET":
        trainees = Trainee.objects.all()
        serializer = TraineeSerializer(trainees,many=True)
        return Response(serializer.data)
    elif request.method =='PUT':
        trainees = Trainee.objects.all()
        serializer = TraineeSerializer(trainees,many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        trainees = Trainer.objects.all()
        serializer = TraineeSerializer(trainees,many=True)
        return Response(serializer.data)
    elif request.method =='DELETE':
        trainees = Trainee.objects.all()
        serializer = TraineeSerializer(trainees,many=True)
        return Response(serializer.data)




@api_view(['GET', 'PUT','POST', 'DELETE'])
def doubtsapi(request):
    if request.method == "GET":
        doubt = Doubts.objects.all()
        serializer = DoubtsSerializer(doubt,many=True)
        return Response(serializer.data)
    elif request.method =='PUT':
        doubt = Doubts.objects.all()
        serializer = DoubtsSerializer(doubt,many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        doubt = Doubts.objects.all()
        serializer = DoubtsSerializer(doubt,many=True)
        return Response(serializer.data)
    elif request.method =='DELETE':
        doubt = Doubts.objects.all()
        serializer = DoubtsSerializer(doubt,many=True)
        return Response(serializer.data)
