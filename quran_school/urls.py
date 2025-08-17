from django.urls import path, include
from . import views
from .api_urls import urlpatterns as api_urlpatterns  # استيراد مسارات الـ API
from .views import ProgressReportAPI  # موجود في api_progress

urlpatterns = [
    # HTML Views
    path('', views.home, name='home'),
    path('tests/', views.test_list, name='test_list'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('payments/', views.payment_list, name='payment_list'),
    path('progress/', views.progress_list, name='progress_list'),

    # API URLs
    path('api/', include(api_urlpatterns)),

    # Progress report API
    path('progress/report/', ProgressReportAPI.as_view(), name='progress-report'),
    path('payments/export/excel/', views.export_payments_excel, name='payments_export_excel'),
    path('payments/export/pdf/', views.export_payments_pdf, name='payments_export_pdf'),
    path('payments/create/<int:student_id>/', views.payment_create, name='payment_create'),

]
