from django.shortcuts import render
from django.http import HttpResponse
from MyApp.models import Trainer,Trainee
from rest_framework.decorators import api_view
from MyApp.serializers import TrainerSerializer,TraineeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


# @api_view(['GET', 'POST', 'DELETE'])
# def home(request):
#     if request.method == 'POST':
#         doubt = Doubts.objects.get() 
#     trainer_Data = Trainer.objects.all()
#     return HttpResponse("This is Home", {'Trainer': trainer_Data})

 
@api_view(['GET', 'PUT','POST', 'DELETE'])
def trainerapi(request):
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

# @api_view(['GET', 'PUT','POST', 'DELETE'])
# def traineeapi(request):
#     if request.method == "GET":
#         trainees = Trainee.objects.all()
#         serializer = TraineeSerializer(trainees,many=True)
#         return Response(serializer.data)
#     elif request.method =='PUT':
#         serializer = TraineeSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()


#     elif request.method =='DELETE':
#         Pass


#     elif request.method =='PUT':
#         Pass

    



