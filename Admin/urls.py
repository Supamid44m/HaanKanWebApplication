from django.db import models
from django.urls import path
from . import views

urlpatterns =[
    path('',views.showuser,name="alluser"),
    path('approveparty',views.approveParty,name="approveparty"),
]