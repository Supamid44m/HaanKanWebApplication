from django.urls import path
from . import views

urlpatterns =[
    path('',views.showNews,name="news"),
    path('<int:id>',views.newsDetail,name="news_detail")
    
]