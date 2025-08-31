from rest_framework import viewsets
from .models import Person, QuranPartTest, MemorizationSession, Attendance
from .serializers import (
    PersonSerializer, QuranPartTestSerializer,
    MemorizationSessionSerializer, AttendanceSerializer
)

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        role = self.request.query_params.get('role')
        if role:
            queryset = queryset.filter(role=role)
        return queryset

from rest_framework import viewsets
from .models import MemorizedPage
from .serializers import MemorizedPageSerializer

class MemorizedPageViewSet(viewsets.ModelViewSet):
    queryset = MemorizedPage.objects.all().order_by('-date')
    serializer_class = MemorizedPageSerializer

class QuranPartTestViewSet(viewsets.ModelViewSet):
    queryset = QuranPartTest.objects.all()
    serializer_class = QuranPartTestSerializer


class MemorizationSessionViewSet(viewsets.ModelViewSet):
    queryset = MemorizationSession.objects.all()
    serializer_class = MemorizationSessionSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
