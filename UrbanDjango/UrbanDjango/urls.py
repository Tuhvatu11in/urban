"""
URL configuration for UrbanDjango project.

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
from task2.views import index, index2
from task4 import views
from task5 import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('1/', index2.as_view()),
    path('2/', index),
    path('3', views.main),
    path('shop/', views.shop),
    path('bill/', views.bill),
    path('', v2.sign_up_by_html),
    path('django_sign_up', v2.sign_up_by_django),

]
