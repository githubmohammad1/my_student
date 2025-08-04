# quran_school/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgressViewSet,ProgressCreateAPIView

router = DefaultRouter()
router.register('progress', ProgressViewSet, basename='progress')

urlpatterns = [
    path('', include(router.urls)),
    path('progress/create/', ProgressCreateAPIView.as_view(), name='progress-create'),
]


# urlpatterns = [
#     path('api/v1/', include(router.urls)),
# ]
