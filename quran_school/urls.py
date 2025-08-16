from django.urls import path
from . import views
from .views import (
    StudentListCreateAPI, StudentDetailAPI,
    TestListCreateAPI, TestDetailAPI,
    AttendanceListCreateAPI, AttendanceDetailAPI,
    AnnouncementListCreateAPI, AnnouncementDetailAPI,
    PaymentListCreateAPI, PaymentDetailAPI,
    ProgressListCreateAPI, ProgressDetailAPI,
)

urlpatterns = [
    # =========================
    #   واجهة HTML (Views عادية)
    # =========================
    path('', views.home, name='home'),

    # Tests HTML
    path('tests/', views.test_list, name='test_list'),

    # Attendance HTML
    path('attendance/', views.attendance_list, name='attendance_list'),

    # Payments HTML
    path('payments/', views.payment_list, name='payment_list'),
    path('payments/create/<int:student_id>/', views.payment_create, name='payment_create'),
    path('payments/<int:pk>/edit/',        views.payment_update, name='payment_update'),
    path('payments/<int:pk>/delete/',      views.payment_delete, name='payment_delete'),
    path('payments/export/csv/',           views.export_payments_csv, name='export_csv'),
    path('payments/export/pdf/',           views.export_payments_pdf, name='export_pdf'),

    # Progress HTML
    path('progress/', views.progress_list, name='progress_list'),


    # =========================
    #   API Endpoints
    # =========================

    # Student API
    path('api/students/',               StudentListCreateAPI.as_view(),   name='student-list'),
    path('api/students/<int:pk>/',      StudentDetailAPI.as_view(),       name='student-detail'),

    # Test API
    path('api/tests/',                  TestListCreateAPI.as_view(),      name='test-list'),
    path('api/tests/<int:pk>/',         TestDetailAPI.as_view(),          name='test-detail'),

    # Attendance API
    path('api/attendances/',            AttendanceListCreateAPI.as_view(), name='attendance-list'),
    path('api/attendances/<int:pk>/',   AttendanceDetailAPI.as_view(),     name='attendance-detail'),

    # Announcement API
    path('api/announcements/',          AnnouncementListCreateAPI.as_view(), name='announcement-list'),
    path('api/announcements/<int:pk>/', AnnouncementDetailAPI.as_view(),    name='announcement-detail'),

    # Payment API
    path('api/payments/',               PaymentListCreateAPI.as_view(),    name='payment-list'),
    path('api/payments/<int:pk>/',      PaymentDetailAPI.as_view(),        name='payment-detail'),

    # Progress API
    path('api/progress/',               ProgressListCreateAPI.as_view(),   name='progress-list'),
    path('api/progress/<int:pk>/',      ProgressDetailAPI.as_view(),       name='progress-detail'),
]
