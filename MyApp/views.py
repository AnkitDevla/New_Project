from django.shortcuts import render
from django.http import HttpResponse
from MyApp.models import  Doubts, Trainer, Trainee


    # trainer_Data = Trainer.objects.all()
    # for data in trainer_Data:
    #     print(data.name)

    # if(request.method == "POST"):
        # trainer_Data = Trainer() 
    #     trainer_Data.name = request.POST('name')
    #     trainer_Data.age = request.POST('age')
    #     trainer_Data.email = request.POST('email')
    #     trainer_Data.contact_no = request.POST('contact_no')
    #     trainer_Data.gender = request.POST('gender')
    #     trainer_Data.save()
    #     return HttpResponseRedirect("This is Home",{'Trainer':trainer_Data})

    

def home(request):
    trainer_Data = Trainer.objects.all()

    # no_of_count = Doubts.objects.filter(question_from__id= 12).count()
    # print(no_of_count)

    # trainer_Data = Trainer(name='Deepak', age=34,email = 'deepak@gmail.com', contact_no=9857473748,gender= 'male')
    # trainer_Data.save()

    # trainer_Data = Trainer.objects.get(id=119)
    # trainer_Data.age = "22"
    # trainer_Data.save()

    # trainer_Data = Trainer.objects.get(id=121)
    # trainer_Data.delete()

    # trainer_Data = Trainer.objects.only("name")
    # print(trainer_Data)
    # for trainer in trainer_Data:
    #     print(trainer.email)
    # trainer_Data = Trainer.objects.filter(age=70)
    # trainer_Data = Trainer.objects.values('name')
    # trainer_Data = Trainer.objects.order_by('age')    
    # trainer_Data = Trainer.objects.values_list('name','age')
    
    # Ordered by the ordering tuple
    # trainer_Data = Trainer.objects.order_by('?')
    # trainer_Data = Trainer.objects.defer('email')
    # trainer_Data = Trainer.objects.only('age')



    # name ends with letter h
    # trainer_Data = Trainer.objects.filter(name__endswith ='h')

    # name ends with letter A
    # trainer_Data = Trainer.objects.filter(name__startswith ='A')

    # exclude age=30 from table
    # trainer_Data = Trainer.objects.exclude(age=30)
    
    
    # doubts_Data = Doubts.objects.filter(answer_by__id=30)
    # for d in doubts_Data:
    #     print(d.name)

    # reverse the order 
    # trainer_Data = Trainer.objects.order_by('age').reverse()[0:5]

    # name and age in tuple
    # trainer_Data = Trainer.objects.values_list('name','age')    


    # count the total number of records in table
    # trainer_Data = Trainer.objects.count()    
    # trainer_Data = Trainer.objects.filter(age__lt=60).order_by('age','-name') 

    # sql query after convert
    # print("SQL Query:" , trainer_Data.query)

    # print the data
    # print(trainer_Data)
    return HttpResponse("This is Home",{'Trainer':trainer_Data})
    # return render (request, 'index.html')



