from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('student/', views.StudentCreateView.as_view()),
    path('thanks/', TemplateView.as_view(template_name = 'createview/thanks.html'), name="thanks"),
    path('student1/', views.StudentCreateView1.as_view()),

    path('update/<int:pk>', views.StudentUpdateView.as_view()),
    path('update1/<int:pk>', views.StudentUpdateView1.as_view()),
    path('update2/<int:pk>', views.StudentUpdateView2.as_view()),

    path('delete/<int:pk>', views.StudentDeleteView.as_view()),
    path('delete1/<int:pk>', views.StudentDeleteView1.as_view()),
]
