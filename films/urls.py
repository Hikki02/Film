from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from django.conf.urls.static import static

from films import settings


schema_view = get_schema_view(
   openapi.Info(
      title="Films API",
      default_version='v1',
      description="Films API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # debug toolbar
    # path('__debug__/', include('debug_toolbar.urls')),
    # apps
    path('', include('apps.comments.urls')),
    path('', include('apps.feedback.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

