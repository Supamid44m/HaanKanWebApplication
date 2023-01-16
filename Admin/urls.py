from django.db import models
from django.urls import path
from . import views

urlpatterns =[
    path('alluser',views.showuser,name="alluser"),
    path('approveparty',views.approveParty,name="approveparty"),
    path('addapp',views.addApps,name="addapps"),
    path('writenews',views.writeNews,name="writenews"),
    
]