from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('template/', include('templateview.urls')),
    path('redirect/', include('redirectview.urls')),
]
