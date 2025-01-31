from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
     path('', home, name='home'),  # <-- Startseite hinzufügen
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)