from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from Content.models import *
from .models import News

# Create your views here.
def showNews(req):
    context={"news":News.objects.all}
    return render(req,'Content/news.html',context)

def newsDetail(req,id):
    context=get_object_or_404(News,pk=id)
    return render(req,'Content/newsdetail.html',{
    'news': get_object_or_404(News, pk=id)
  })

