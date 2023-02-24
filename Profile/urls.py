from django.urls import path
from . import views

urlpatterns =[
    path('edit/',views.editprofile,name='editprofile'),
    path('<int:user_id>/',views.profiledetail,name='profile'),
    path('<int:user_id>/like/',views.like_profile,name='like_profile'),
    path('<int:user_id>/unlike/',views.unlike_profile,name='unlike_profile'),
    path('<int:user_id>/dislike/', views.dislike_profile, name='dislike_profile'),
    path('<int:user_id>/undislike/', views.undislike_profile, name='undislike_profile'),
    
]