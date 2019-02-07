"""learning_log URL Configuration
    1. Import the include() function: from django.urls import include, path

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
app_name = 'users'
urlpatterns = [
    #login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    #logout page
    path('logout/',  views.logout_view, name='logout'),
    #registration page
    path('register/', views.register, name='register'),
]
