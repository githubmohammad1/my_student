from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Quran School API",
        default_version='v1',
        description="توثيق API لمشروع المدرسة القرآنية",
        contact=openapi.Contact(email="admin@example.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quran_school.urls')),
    # path('api/v1/', include('quran_school.api.urls')),
    path('api-token-auth/', obtain_auth_token),  # ✅ نقطة المصادقة
]
urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
###