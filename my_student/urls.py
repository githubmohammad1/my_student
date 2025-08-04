from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quran_school.urls')),
    path('api/v1/', include('quran_school.api.urls')),
]
