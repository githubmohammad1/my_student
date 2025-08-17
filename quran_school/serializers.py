from rest_framework import serializers
from .models import (
    Student, Test, Attendance,
    Announcement, MonthlyPayment
)

# 🔹 الطالب
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


# 🔹 الاختبار
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


# 🔹 الحضور (مع تضمين بيانات الطالب والاختبار)
class AttendanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    test = TestSerializer(read_only=True)
    period_display = serializers.CharField(source='get_period_display', read_only=True)

    class Meta:
        model = Attendance
        fields = '__all__'


# 🔹 الإعلان
class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


# 🔹 المدفوعات الشهرية
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyPayment
        fields = '__all__'


# 🔹 التقدم (مستخرج من الحضور)
class ProgressSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = [
            'student',        # بيانات الطالب
            'date',           # التاريخ
            'pages_listened', # عدد الصفحات المسموعة
            'page_note',      # ملاحظة رقم الصفحة
            'tested',         # هل اختبر
            'test'            # رابط الاختبار
        ]
