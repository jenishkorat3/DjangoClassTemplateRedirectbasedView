from django.urls import path
from django.views.generic.base import TemplateView, RedirectView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name="core/home.html"), name="main"),
    path('home', RedirectView.as_view(url="/")),
    path('home/1', views.RedirectView.as_view(pattern_name="house")),
    path('index/', views.HomeRedirectView.as_view()),
    path('login/<int:pk>/', TemplateView.as_view(template_name="core/news.html"), name="login"),
    path('success/<int:pk>/', views.SuccessRedirectView.as_view(), name="main"),
]
