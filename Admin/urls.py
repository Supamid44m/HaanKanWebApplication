from django.db import models
from django.urls import path
from . import views

urlpatterns =[
    path('alluser',views.showuser,name="alluser"),
    path('approveparty',views.approveParty,name="approveparty"),
    path('approve/<int:party_id>/', views.approve_party, name='approve_party'),
    path('reject/<int:party_id>/', views.reject_party, name='reject_party'),
    path('delete/<int:party_id>/', views.delte_party, name='delete_party'),
    path('applist', views.showApps, name='apps_list'),
    path('app/approve/<int:app_id>', views.approve_app, name='approve_app'),
    path('app/reject/<int:app_id>', views.reject_app, name='reject_app'),
    path('app/delete/<int:app_id>', views.delete_app, name='delete_app'),
    path('app/<int:app_id>/update/', views.edit_app, name='edit_app'),
    path('banklist', views.showBanks, name='banks_list'),
    path('addbank/', views.addBanks, name='addbanks'),
    path('bank/delete/<int:bank_id>', views.delete_bank, name='delete_bank'),
    path('bank/<int:bank_id>/update/', views.edit_bank, name='edit_bank'),
    path('editprofile/<int:user_id>/', views.editprofile, name='edit_profileAd'),
    path('deleteuser/<int:user_id>/',views.delete_user,name='delete_user'),
    path('writenews',views.writeNews,name="writenews"),



    #path('app/approve/<int:app_id>/', views.approve_app, name='approve_app'),
    #path('app/reject/<int:app_id>/', views.reject_app, name='reject_app'),
    #path('app/delete/<int:app_id>/', views.delete_app, name='delete_app'),
    
]