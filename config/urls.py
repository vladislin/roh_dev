from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
    path('sitemap.xml/', TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml"),),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
