# ocr/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_photo

urlpatterns = [
    path('upload/', upload_photo, name='upload_photo')
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
