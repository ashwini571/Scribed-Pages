from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('notebook.urls')),
      path('accounts/', include('accounts.urls')),
      path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
