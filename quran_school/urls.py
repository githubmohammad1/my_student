from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tests/', views.test_list, name='test_list'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('payments/', views.payment_list, name='payment_list'),
    path('payments/create/<int:student_id>/', views.payment_create, name='payment_create'),
    path('payments/<int:pk>/edit/',        views.payment_update, name='payment_update'),
    path('payments/<int:pk>/delete/',      views.payment_delete, name='payment_delete'),
    path('payments/export/csv/',           views.export_payments_csv, name='export_csv'),
    path('payments/export/pdf/',           views.export_payments_pdf, name='export_pdf'),
    path('progress/', views.progress_list, name='progress_list'),
    
]
