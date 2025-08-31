from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PersonViewSet, QuranPartTestViewSet,
    MemorizationSessionViewSet, AttendanceViewSet
)
from .views import MemorizedPageViewSet

router = DefaultRouter()
router.register(r'memorized-pages', MemorizedPageViewSet)

router.register(r'persons', PersonViewSet)
router.register(r'quran-tests', QuranPartTestViewSet)
router.register(r'memorization-sessions', MemorizationSessionViewSet)
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
