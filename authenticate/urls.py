from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin



urlpatterns = [
   
    path('/',include('djoser.urls')),
    path('/', include('djoser.urls.authtoken')),
]
