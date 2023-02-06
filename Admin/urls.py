from django.db import models
from django.urls import path
from . import views

urlpatterns =[
    path('alluser',views.showuser,name="alluser"),
    path('approveparty',views.approveParty,name="approveparty"),
    path('approve/<int:party_id>/', views.approve_party, name='approve_party'),
    path('reject/<int:party_id>/', views.reject_party, name='reject_party'),
    path('delete/<int:party_id>/', views.delte_party, name='delete_party'),
    path('addapp',views.addApps,name="addapps"),
    path('addapp/approve/<int:app_id>/', views.approve_app, name='approve_app'),
    path('addapp/reject/<int:app_id>/', views.reject_app, name='reject_app'),
    path('addapp/delete/<int:app_id>/', views.delete_app, name='delete_app'),
    path('writenews',views.writeNews,name="writenews"),
    
]