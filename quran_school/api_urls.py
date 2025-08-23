from django.urls import path





from .views import (
    StudentListCreateAPI , StudentDetailAPI,
    TestListCreateAPI, TestDetailAPI,
    AttendanceListCreateAPI, AttendanceDetailAPI,
    AnnouncementListCreateAPI, AnnouncementDetailAPI,
    PaymentListCreateAPI, PaymentDetailAPI,
    ProgressListCreateAPI, ProgressDetailAPI,
    ProgressReportAPI
)


urlpatterns = [

   # يعيد التوكين عند إرسال username/password
    # Student API
    path('students/', StudentListCreateAPI.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailAPI.as_view(), name='student-detail'),

    # Test API
    path('tests/', TestListCreateAPI.as_view(), name='test-list'),
    path('tests/<int:pk>/', TestDetailAPI.as_view(), name='test-detail'),

    # Attendance API
    path('attendances/', AttendanceListCreateAPI.as_view(), name='attendance-list'),
    path('attendances/<int:pk>/', AttendanceDetailAPI.as_view(), name='attendance-detail'),

    # Announcement API
    path('announcements/', AnnouncementListCreateAPI.as_view(), name='announcement-list'),
    path('announcements/<int:pk>/', AnnouncementDetailAPI.as_view(), name='announcement-detail'),

    # Payment API
    path('payments/', PaymentListCreateAPI.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentDetailAPI.as_view(), name='payment-detail'),

    # Progress API
    path('progress/', ProgressListCreateAPI.as_view(), name='progress-list'),
    path('progress/<int:pk>/', ProgressDetailAPI.as_view(), name='progress-detail'),

    # Progress Report API
    path('progress/report/', ProgressReportAPI.as_view(), name='progress-report'),
]
