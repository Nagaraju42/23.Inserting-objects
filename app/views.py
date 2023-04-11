from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def insert_topic(request):
    tn=input('enter topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic name inserted successfully')


def insert_Webpage(request):
    tn=input('enter topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=input('enter name : ')
    WO=input('enter url : ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('name inserted successfully')

def insert_AR(request):
    tn=input('enter topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=input('enter name : ')
    WO=input('enter url : ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    tn=input('enter author : ')
    tn=input('enter date : ')
    ARO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    ARO.save()
    return HttpResponse('author inserted successfully')

