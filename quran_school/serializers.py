from rest_framework import serializers
from .models import (
    Student, Test, Attendance,
    Announcement, MonthlyPayment
)
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student

class StudentRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    name = serializers.CharField()
    father_name = serializers.CharField(allow_blank=True, required=False)
    age = serializers.IntegerField()
    current_grade = serializers.CharField()
    whatsapp = serializers.CharField()
    nearest_address = serializers.CharField(allow_blank=True, required=False)
    registration_date = serializers.DateField()

    def create(self, validated_data):
        # إنشاء مستخدم النظام
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # إنشاء الطالب وربطه بالمستخدم
        student = Student.objects.create(
            name=validated_data['name'],
            father_name=validated_data.get('father_name', ''),
            age=validated_data['age'],
            current_grade=validated_data['current_grade'],
            whatsapp=validated_data['whatsapp'],
            nearest_address=validated_data.get('nearest_address', ''),
            registration_date=validated_data['registration_date'],
            status='active'
        )
        return user, student

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
