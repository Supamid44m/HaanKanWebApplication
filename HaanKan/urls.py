from django.contrib import admin
from django.urls import path,include,re_path
from django.shortcuts import render, redirect
from django.conf.urls.static import static
from django.conf import settings
from Party import consumers
from Admin import views 
from Authenticate import views as authview

urlpatterns = [
    
    path("party/", include('Party.urls')),
    path("admin/", admin.site.urls),
    path("Admin/", include('Admin.urls')),
    path('news/', include('Content.urls')),
    path('profile/', include('Profile.urls')),
    path('accounts/', include('allauth.urls')),
    #path('', include('Authenticate.urls')),
    path("authenticate/",include("django.contrib.auth.urls")),
    path('app',views.addApps,name="addapps"),
    path("",authview.login_user,name="login_user"),
    path("register",authview.register,name="register"),
    path("changepassword",authview.change_password,name="change_password")
   
    
    
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)