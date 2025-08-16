# quran_school/views.py

# ======================
#  Imports مشتركة
# ======================
from datetime import date
from io import BytesIO
import csv

from django.db.models import Q, Prefetch, Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

from .forms import PaymentForm
from .models import (
    Student, Test, Attendance,
    Announcement, MonthlyPayment
)

# ======================
#  استيرادات API
# ======================
from rest_framework import generics
from .serializers import (
    StudentSerializer, TestSerializer,
    AttendanceSerializer, AnnouncementSerializer,
    PaymentSerializer, ProgressSerializer
)

# ======================
#   القسم الأول: API Views
# ======================

# Student Endpoints
class StudentListCreateAPI(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Test Endpoints
class TestListCreateAPI(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

# Attendance Endpoints
class AttendanceListCreateAPI(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

# Announcement Endpoints
class AnnouncementListCreateAPI(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class AnnouncementDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

# Payment Endpoints
class PaymentListCreateAPI(generics.ListCreateAPIView):
    queryset = MonthlyPayment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonthlyPayment.objects.all()
    serializer_class = PaymentSerializer

# Progress Endpoints
class ProgressListCreateAPI(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = ProgressSerializer

class ProgressDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = ProgressSerializer


# ======================
#   القسم الثاني: HTML Views
# ======================

def home(request):
    announcements = Announcement.objects.all().order_by('-date')
    return render(request, 'quran_school/home.html', {
        'announcements': announcements,
    })

def test_list(request):
    tests = Test.objects.all().order_by('-date')
    return render(request, 'quran_school/test_list.html', {
        'tests': tests,
    })

def attendance_list(request):
    records = Attendance.objects.all().order_by('-date')
    return render(request, 'quran_school/attendance_list.html', {
        'records': records,
    })

def _filter_payments_and_students(request):
    month_str = request.GET.get('month', '').strip()
    student_q = request.GET.get('student', '').strip()

    payments_qs = MonthlyPayment.objects.all().order_by('-date')

    date_filter = None
    if month_str:
        try:
            year, month_num = map(int, month_str.split('-'))
            payments_qs = payments_qs.filter(date__year=year, date__month=month_num)
            date_filter = Q(payments__date__year=year, payments__date__month=month_num)
        except ValueError:
            date_filter = None

    if date_filter:
        students = Student.objects.annotate(
            total_paid=Sum('payments__amount', filter=date_filter)
        )
    else:
        students = Student.objects.annotate(
            total_paid=Sum('payments__amount')
        )

    students = students.prefetch_related(
        Prefetch('payments', queryset=payments_qs)
    )

    if student_q:
        students = students.filter(name__icontains=student_q)

    overall_total = payments_qs.aggregate(total=Sum('amount'))['total'] or 0

    return students, payments_qs, overall_total, month_str, student_q

def payment_list(request):
    students, payments_qs, overall, month_str, student_q = _filter_payments_and_students(request)
    return render(request, 'quran_school/payment_list.html', {
        'students':       students,
        'payments':       payments_qs,
        'overall_total':  overall,
        'selected_month': month_str,
        'student_query':  student_q,
    })

def payment_create(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.student = student
            payment.save()
            return redirect('payment_list')
    else:
        form = PaymentForm(initial={'date': date.today()})
    return render(request, 'quran_school/payment_form.html', {
        'form':    form,
        'student': student,
    })

def payment_update(request, pk):
    payment = get_object_or_404(MonthlyPayment, pk=pk)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'quran_school/payment_form.html', {
        'form':    form,
        'student': payment.student,
    })

def payment_delete(request, pk):
    payment = get_object_or_404(MonthlyPayment, pk=pk)
    payment.delete()
    return redirect('payment_list')

def export_payments_csv(request):
    _, payments_qs, _, _, _ = _filter_payments_and_students(request)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="payments.csv"'
    writer = csv.writer(response)
    writer.writerow(['#', 'اسم الطالب', 'التاريخ', 'المبلغ'])
    for idx, pay in enumerate(payments_qs, start=1):
        writer.writerow([idx, pay.student.name, pay.date.strftime("%Y-%m-%d"), f"{pay.amount:.2f}"])
    return response

def export_payments_pdf(request):
    _, payments_qs, overall, _, _ = _filter_payments_and_students(request)
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=A4,
        rightMargin=2*cm, leftMargin=2*cm,
        topMargin=2*cm, bottomMargin=2*cm
    )
    styles = getSampleStyleSheet()
    elements = []
    elements.append(Paragraph("تقرير المدفوعات", styles['Title']))
    elements.append(Spacer(1, 0.5*cm))
    data = [["#", "اسم الطالب", "التاريخ", "المبلغ (ر.س)"]]
    for idx, pay in enumerate(payments_qs, start=1):
        data.append([idx, pay.student.name, pay.date.strftime("%Y-%m-%d"), f"{pay.amount:.2f}"])
    data.append(["", "", "المجموع الكلي", f"{overall:.2f}"])
    table = Table(data, colWidths=[1.5*cm, 6*cm, 4*cm, 3*cm])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ALIGN', (3, 1), (3, -1), 'RIGHT'),
        ('SPAN', (0, len(data)-1), (2, len(data)-1)),
        ('ALIGN', (0, len(data)-1), (2, len(data)-1), 'RIGHT'),
        ('FONTNAME', (0, len(data)-1), (-1, len(data)-1), 'Helvetica-Bold'),
    ]))
    elements.append(table)
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="payments_report.pdf"'
    return response

def progress_list(request):
    student_q = request.GET.get('student', '').strip()

    # جلب سجلات الحضور مع جلب بيانات الطالب المرتبطة لتقليل الاستعلامات
    qs = Attendance.objects.select_related('student')

    # فلترة حسب اسم الطالب إذا كان موجودًا في البحث
    if student_q:
        qs = qs.filter(student__name__icontains=student_q)

    # عرض النتائج في القالب
    return render(request, 'quran_school/progress_list.html', {
        'records': qs,
        'student_query': student_q,
    })
