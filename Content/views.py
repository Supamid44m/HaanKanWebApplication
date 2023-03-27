from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from Content.models import *
from .models import News
from Admin.forms import WriteNewsforms

# Create your views here.
def showNews(req):
    context={"news":News.objects.all()}
    return render(req,'Content/news.html',context)

def newsDetail(req,id):
    context=get_object_or_404(News,pk=id)
    return render(req,'Content/newsdetail.html',{
    'news': get_object_or_404(News, pk=id)
  })

def like_news(req, id):
    if req.user.is_authenticated:
        user = req.user
        news = get_object_or_404(News, pk=id)
        news.like_news(user)
        return redirect("/news/"+ str(id))
    else:
      return redirect("/news/"+ str(id))


def unlike_news(req, id):
    if req.user.is_authenticated:
        news = get_object_or_404(News, pk=id)
        news.unlike_news(req.user)
        return redirect("/news/"+ str(id))
    else:
      return redirect("/news/"+ str(id))

def dislike_news(req, id):
    if req.user.is_authenticated:
        news = get_object_or_404(News, pk=id)
        news.dislike_news(req.user)
        return redirect("/news/"+ str(id))
    else:
      return redirect("/news/"+ str(id))


def undislike_news(req, id):
    if req.user.is_authenticated:
        news = get_object_or_404(News, pk=id)
        news.undislike_news(req.user)
        return redirect("/news/"+ str(id))
    else:
      return redirect("/news/"+ str(id))


def delete_news(req,id):
    news= get_object_or_404(News,pk=id)
    if req.user.is_superuser and req.method == "POST":
        news.delete()
        return redirect('/news/')
    

def edit_news(req,id):
    print(id)
    if req.user.is_superuser:
        new=get_object_or_404(News,pk=id)
        form=WriteNewsforms(req.POST or None ,req.FILES or None,instance=new)
        if form.is_valid():
            writer=form.save()
            writer.writer = req.user
            writer.save()
            return redirect('/news/')
        else:
            new=get_object_or_404(News,pk=id)
            form=WriteNewsforms(req.POST or None ,req.FILES or None,instance=new)
        return render(req, 'Admin/editnews.html', {'news': new, 'form': form})
    
    else:
        return redirect('party')