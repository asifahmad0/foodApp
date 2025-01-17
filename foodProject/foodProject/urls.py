"""
URL configuration for foodProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from foodApp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='Home'),
    path('about/',about, name='About'),
    path('book/',book, name='Book'),
    path('menu/',menu, name='Menu'),
    path('feedback/',feedback, name='Feedback'),
    path('profile/',profile, name='Profile'),
    path('loginn/',loginn, name='Login'),
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

