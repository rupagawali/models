from django.shortcuts import render
from django.db.models.functions import Length

# Create your views here.
from app.models import *
from django.http import HttpResponse
def topic(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'topic.html',d)

def webpage(request):
    QLWO=WebPage.objects.all()
    d={'webpages':QLWO}
    return render(request,'webpage.html',d)

def accessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={'accessrecords':QLAO}
    return render(request,'accessrecord.html',d)

def insert_topic(request):
    tn=input('enter topic_name')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'topic.html',d)

def insert_webpage(request):
    tn=input('enter topicname')
    n=input('enter name')
    u=input('enter url')
    TO=Topic.objects.get(topic_name=tn)
    NWO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    NWO.save()
    QLWO=WebPage.objects.all()
    d={'webpage':QLWO}
    return render(request,'webpage.html',d)

def insert_accessrecord(request):
    pk=int(input('pk'))
    d=input('date')
    a=input('author')
    wo=WebPage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=wo,date=d,author=a)[0]
    NAO.save()
    QLAO=AccessRecord.objects.all()
    d={'accessrecords':QLAO}
    return render(request,'accessrecord.html',d)

def update_webpage(request):
    #WebPage.objects.filter(topic_name='cricket').update(name='Rohit Sharma')
    #WebPage.objects.filter(topic_name='fb').update(url='http:///aaa.in')
    #WebPage.objects.filter(topic_name='A').update(name='Rohit Sharma')
    WebPage.objects.update_or_create(topic_name='cricket',defaults={'name':'A','url':'http://zz.in'})

    QLWO=WebPage.objects.all()
    d={'webpage':QLWO}
    return render(request,'webpage.html',d)

def delete(request):
    s=Rupa.objects.all()
    