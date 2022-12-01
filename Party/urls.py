from django.urls import path
from . import views


urlpatterns =[
    path('',views.showParty,name="party"),
    path('create/',views.crateParty,name='createParty')
    
]