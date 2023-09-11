from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


# Define a Swagger schema view for API documentation.
schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Blog",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,  # Make the documentation publicly accessible.
    permission_classes=[AllowAny]  # Allow any user to access the documentation.
)

# Define URL patterns for your Django project.
urlpatterns = [
    # Admin site URL.
    path("admin/", admin.site.urls),

    # API endpoints URL. This includes the 'app.urls' module.
    path("api/", include("app.urls")),

    # URL for Swagger documentation with Swagger UI.
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),

    # URL for ReDoc documentation with ReDoc UI.
    path('redoc/', schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc-ui"),
]

# Add URL patterns for serving media files.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add URL patterns for serving static files.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

