"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from Photogallery import views




urlpatterns = [
url(r'^$', views.index, name='index'),

url(r'^item/(?P<item_Id>[0-9]+)', views.item, name='item'),
url('upload/', views.simple_upload, name='upload'),
url('uploadform/', views.upload_file, name='uploadform'),
url('Country_View/', views.showPicturesfromCountry, name='Country_view'),



]
