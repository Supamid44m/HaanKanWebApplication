from django.urls import path ,include
from . import views


urlpatterns =[
    #path("",include("django.contrib.auth.urls")),
    path("login_user",views.login_user,name="login_user"),
    path("register",views.register,name="register")
]