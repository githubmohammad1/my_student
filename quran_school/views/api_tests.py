from rest_framework import generics
from ..models import Test
from ..serializers import TestSerializer

class TestListCreateAPI(generics.ListCreateAPIView):
    queryset = Test.objects.all().order_by('-date')
    serializer_class = TestSerializer

class TestDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
