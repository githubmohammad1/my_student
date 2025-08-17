from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Attendance
from ..serializers import AttendanceSerializer

class AttendanceListCreateAPI(generics.ListCreateAPIView):
    queryset = Attendance.objects.all().order_by('-date')
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['student', 'period', 'tested', 'date']
    search_fields = ['student__name', 'page_note']
    ordering_fields = ['date', 'pages_listened']

class AttendanceDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
