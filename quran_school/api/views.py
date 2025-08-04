from rest_framework import generics, permissions

from ..models import (
    Student, Test, Attendance,
    Announcement, Payment, Progress
)


from .serializers import (
    StudentSerializer, TestSerializer,
    AttendanceSerializer, AnnouncementSerializer,
    PaymentSerializer, ProgressSerializer
)

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
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


# Progress Endpoints
class ProgressListCreateAPI(generics.ListCreateAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer


class ProgressDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
