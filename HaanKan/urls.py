from django.contrib import admin
from django.urls import path,include,re_path
from django.shortcuts import render, redirect
from django.conf.urls.static import static
from django.conf import settings
from Party import consumers



urlpatterns = [
    path("party/", include('Party.urls')),
    path("admin/", admin.site.urls),
    path("Admin/", include('Admin.urls')),
    path('user/', include('Authenticate.urls')),
    path('news/', include('Content.urls')),
    path('profile/', include('Profile.urls')),
    path('accounts/', include('allauth.urls')),
    
    
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)