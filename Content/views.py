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

def like_news(request, id):
    user = request.user
    news = get_object_or_404(News, pk=id)
    news.like_news(user)
    return redirect("/news/"+ str(id))


def unlike_news(request, id):
    news = get_object_or_404(News, pk=id)
    news.unlike_news(request.user)
    return redirect("/news/"+ str(id))


def dislike_news(request, id):
    news = get_object_or_404(News, pk=id)
    news.dislike_news(request.user)
    return redirect("/news/"+ str(id))


def undislike_news(request, id):
    news = get_object_or_404(News, pk=id)
    news.undislike_news(request.user)
    return redirect("/news/"+ str(id))

def delete_news(req,id):
    news= get_object_or_404(News,pk=id)
    if req.user.is_superuser and req.method == "POST":
        news.delete()
        return redirect('/news/')
    

