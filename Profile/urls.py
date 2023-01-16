from django.urls import path
from . import views

urlpatterns =[
    path('edit/',views.editprofile,name='profiledetail'),
    path('<int:id>/detail',views.profiledetail,name='profiledetail'),
    
]