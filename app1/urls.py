"""miniproj2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.index, name="index"),
    path('logout', views.logoutuser, name="logoutuser"),
    path('tenantregister', views.tenantRegister, name="tenantRegister"),
    path('landlorddash', views.landlorddash, name="landlorddash"),
    path('landlordregister', views.landlordRegister, name="landlordRegister"),
    path('bookproperty/<int:id>/<slug:userid>', views.bookproperty, name="bookproperty"),
    path('removeproperty/<int:id>', views.removeproperty, name="removeproperty"),
    path('uploadproperty', views.uploadproperty, name="uploadproperty"),
    path('deleteproperty/<int:id>', views.deleteproperty, name="deleteproperty"),
    path('userdash', views.userdashboard, name="userdashboard"),
    path('register', views.register, name="register"),
    path('home', views.home, name="home"),
    path('searchresult', views.searchresult, name="searchresult"),
]
