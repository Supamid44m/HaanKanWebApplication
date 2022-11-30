from django.http.response import HttpResponse
from django.shortcuts import render
from Content.models import *

# Create your views here.
def showNews(req):
    context={"News":News.objects.all()}
    return render(req,'Content/header.html',context={})
