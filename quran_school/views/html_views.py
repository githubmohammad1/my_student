from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models import Announcement, Test, Attendance, MonthlyPayment, Student
from ..forms import PaymentForm
import openpyxl
from reportlab.pdfgen import canvas

# 🏠 الصفحة الرئيسية
def home(request):
    announcements = Announcement.objects.all().order_by('-date')
    return render(request, 'quran_school/home.html', {
        'announcements': announcements
    })

# 📘 قائمة الاختبارات
def test_list(request):
    tests = Test.objects.all().order_by('-date')
    return render(request, 'quran_school/test_list.html', {
        'tests': tests
    })

# 📋 قائمة الحضور والغياب
def attendance_list(request):
    records = Attendance.objects.all().order_by('-date')
    return render(request, 'quran_school/attendance_list.html', {
        'records': records
    })

# 📊 قائمة التقدم (فلترة باسم الطالب)
def progress_list(request):
    student_q = request.GET.get('student', '').strip()
    qs = Attendance.objects.select_related('student')
    if student_q:
        qs = qs.filter(student__name__icontains=student_q)
    return render(request, 'quran_school/progress_list.html', {
        'records': qs,
        'student_query': student_q,
    })

# 📤 تصدير الدفعات إلى Excel
def export_payments_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "تقرير الدفعات"

    ws.append(["اسم الطالب", "التاريخ", "المبلغ"])
    for p in MonthlyPayment.objects.select_related('student'):
        ws.append([p.student.name, p.date.strftime("%Y-%m-%d"), p.amount])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response['Content-Disposition'] = 'attachment; filename="payments.xlsx"'
    wb.save(response)
    return response

# 📄 تصدير الدفعات إلى PDF
def export_payments_pdf(request):
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="payments.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica", 14)
    p.drawString(100, 800, "تقرير الدفعات")

    y = 770
    for pay in MonthlyPayment.objects.select_related('student'):
        p.drawString(100, y, f"{pay.student.name} - {pay.date.strftime('%Y-%m-%d')} - {pay.amount}")
        y -= 20

    p.showPage()
    p.save()
    return response

# ➕ إنشاء دفعة جديدة لطالب
def payment_create(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.student = student
            payment.save()
            return redirect('payment_list')  # تأكد أن هذا الاسم موجود في urls.py
    else:
        form = PaymentForm()
    return render(request, 'quran_school/payment_form.html', {
        'form': form,
        'student': student
    })
import calendar
from django.db.models import Sum
from collections import defaultdict



def payments_list(request):
    students = Student.objects.all()
    months = list(range(1, 13))  # [1, 2, ..., 12]
    month_names = [calendar.month_name[m] for m in months]  # أسماء الشهور بالعربية إذا كانت لغة النظام عربية

    for s in students:
        s.payments_by_month = {}
        for m in months:
            total = s.payments.filter(date__month=m).aggregate(total=Sum('amount'))['total']
            s.payments_by_month[m] = total if total else None

    return render(request, 'payments_list.html', {
        'students': students,
        'months': month_names
    })
