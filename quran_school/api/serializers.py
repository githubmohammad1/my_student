from rest_framework import serializers
from ..models import (
    Student, Test, Attendance,
    Announcement, Payment, Progress
)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'
