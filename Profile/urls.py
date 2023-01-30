from django.urls import path
from . import views

urlpatterns =[
    path('edit/',views.editprofile,name='editprofile'),
    path('<int:id>/detail',views.profiledetail,name='profiledetail'),
    
]