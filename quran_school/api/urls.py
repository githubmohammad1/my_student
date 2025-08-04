# quran_school/api/urls.py
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ProgressViewSet,ProgressCreateAPIView

# router = DefaultRouter()
# router.register('progress', ProgressViewSet, basename='progress')

# urlpatterns = [
#     path('', include(router.urls)),
# ]



from django.urls import path
from .views import (
    StudentListCreateAPI, StudentDetailAPI,
    TestListCreateAPI, TestDetailAPI,
    AttendanceListCreateAPI, AttendanceDetailAPI,
    AnnouncementListCreateAPI, AnnouncementDetailAPI,
    PaymentListCreateAPI, PaymentDetailAPI,
    ProgressListCreateAPI, ProgressDetailAPI,
)

urlpatterns = [
    # Student endpoints
    path('students/',               StudentListCreateAPI.as_view(),   name='student-list'),
    path('students/<int:pk>/',      StudentDetailAPI.as_view(),       name='student-detail'),

    # Test endpoints
    path('tests/',                  TestListCreateAPI.as_view(),      name='test-list'),
    path('tests/<int:pk>/',         TestDetailAPI.as_view(),          name='test-detail'),

    # Attendance endpoints
    path('attendances/',            AttendanceListCreateAPI.as_view(), name='attendance-list'),
    path('attendances/<int:pk>/',   AttendanceDetailAPI.as_view(),     name='attendance-detail'),

    # Announcement endpoints
    path('announcements/',          AnnouncementListCreateAPI.as_view(), name='announcement-list'),
    path('announcements/<int:pk>/', AnnouncementDetailAPI.as_view(),    name='announcement-detail'),

    # Payment endpoints
    path('payments/',               PaymentListCreateAPI.as_view(),    name='payment-list'),
    path('payments/<int:pk>/',      PaymentDetailAPI.as_view(),        name='payment-detail'),

    # Progress endpoints
    path('progress/',               ProgressListCreateAPI.as_view(),   name='progress-list'),
    path('progress/<int:pk>/',      ProgressDetailAPI.as_view(),       name='progress-detail'),
]
