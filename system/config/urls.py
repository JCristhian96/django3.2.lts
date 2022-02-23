from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# Docs for API
from drf_yasg.views import get_schema_view
from drf_yasg import openapi 

schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion API",
      default_version='v0.1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Urls for Swagger
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Debug Toolbar
if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),