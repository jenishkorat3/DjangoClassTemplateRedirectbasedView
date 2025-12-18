"""
URL configuration for djangoclassview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('home/', views.home, name="home"),
    path('context/', views.context, name="context"),
    path('news/', views.news, {'template_name': 'core/news.html'}, name="news"),
    path('news2/', views.news, {'template_name': 'core/news2.html'}, name="news2"),
    path('contact/', views.contact, name="contact"),


    path('mainclass/', views.MainClass.as_view(), name="mainclass"),
    path('homeclass/', views.HomeClass.as_view(), name="homeclass"),
    path('contextclass/', views.ContextClass.as_view(), name="contextclass"),
    path('contextclass2/', views.ContextClass2.as_view(), name="contextclass2"),
    path('newsclass/', views.NewsClass.as_view(), {'template_name': 'core/news.html'}, name="newsclass"),
    path('newsclass2/', views.NewsClass.as_view(), {'template_name': 'core/news2.html'}, name="newsclass2"),
    path('contactclass/', views.ContactClass.as_view(), name="contactclass"),
]
