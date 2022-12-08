from django.http.response import HttpResponse
from django.shortcuts import render
from Content.models import *

# Create your views here.
def showNews(req):
    """  news=None
    try:
        news=News.objects.all()
    except News.DoesNotExist:
        news=None"""
   
    context={"news":News.objects.all}
    return render(req,'Content/news.html',context)
