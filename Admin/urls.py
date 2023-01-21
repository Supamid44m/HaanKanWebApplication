from django.db import models
from django.urls import path
from . import views

urlpatterns =[
    path('alluser',views.showuser,name="alluser"),
    path('approveparty',views.approveParty,name="approveparty"),
    path('approve/<int:party_id>/', views.approve_party, name='approve_party'),
    path('reject/<int:party_id>/', views.reject_party, name='reject_party'),
    path('delete/<int:party_id>/', views.reject_party, name='delete_party'),
    path('addapp',views.addApps,name="addapps"),
    path('writenews',views.writeNews,name="writenews"),
    
]