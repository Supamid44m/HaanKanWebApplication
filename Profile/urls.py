from django.urls import path
from . import views

urlpatterns =[
    path('edit/',views.editprofile,name='editprofile'),
    path('<int:user_id>/',views.profiledetail,name='profile'),
    
]