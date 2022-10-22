"""todolist URL Configuration"""
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from todolist.view import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', health_check, name='health-check'),
    path('core/', include('core.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('goals/', include('goals.urls')),
    path('bot/', include('bot.urls')),
    path('swagger/schema-download/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema')),
]
