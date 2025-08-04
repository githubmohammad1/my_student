# quran_school/api/views.py
from rest_framework import viewsets
from quran_school.models import Progress
from .serializers import ProgressSerializer


class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.select_related('student').all()
    serializer_class = ProgressSerializer

# quran_school/api/views.py
from rest_framework.generics import CreateAPIView

class ProgressCreateAPIView(CreateAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
