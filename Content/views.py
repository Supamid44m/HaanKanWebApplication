from django.http.response import HttpResponse
from django.shortcuts import render
from Content.models import *

# Create your views here.
def showNews(req):
    context={"news":News.objects.all()}
    return render(req,'Content/news.html',context)
