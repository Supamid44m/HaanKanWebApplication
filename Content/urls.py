from django.urls import path
from . import views

urlpatterns =[
    path('',views.showNews,name="news"),
    path('<int:id>',views.newsDetail,name="news_detail"),
    path('<int:id>/like/', views.like_news, name='like_news'),
    path('<int:id>/unlike/', views.unlike_news, name='unlike_news'),
    path('<int:id>/dislike/', views.dislike_news, name='dislike_news'),
    path('<int:id>/undislike/', views.undislike_news, name='undislike_news'),
    path('<int:id>/delete',views.delete_news,name='delete_news'),
    path('<int:id>/update/',views.edit_news,name='edit_news')
    
]