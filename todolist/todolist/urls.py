from xml.dom.expatbuilder import Namespaces
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')), 
    path('oauth/', include('social_django.urls', namespace="social")),
    path('goals/', include('goals.urls')),
    path('/bot', include('bot.urls')),
]
