from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def Insert_Topic(request):
    TN=input('Enter a topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=TN)[0]
    TO.save()
    return HttpResponse('Topic_name inserted successfully')


def Insert_webpage(request):
    TN = input('Enter topic_name : ')
    TO = Topic.objects.get(topic_name=TN)
    name = input('Enter a name : ')
    url = input('Enter url : ')
    WO=webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
    WO.save()
    return HttpResponse('Data inserted to webpage successfully')


def Insert_AR(request):
    TN = input('Enter topic_name : ')
    TO =  Topic.objects.get(topic_name=TN)
    name = input('Enter name : ')
    WO = webpage.objects.get(name=name)
    date = input('Enter date YYYY-MM-DD')
    author = input('Enter author : ')
    email = input('Entre email : ')
    ARO = AccessRecord.objects.get_or_create(name=WO,date=date,author=author,email=email)[0]
    ARO.save()
    return HttpResponse('Data insterd to Accessrecords successfully')