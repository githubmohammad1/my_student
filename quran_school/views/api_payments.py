from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from ..models import MonthlyPayment
from ..serializers import PaymentSerializer

class PaymentListCreateAPI(generics.ListCreateAPIView):
    queryset = MonthlyPayment.objects.all().order_by('-year', '-month')
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['student', 'month', 'year', 'is_paid']
    ordering_fields = ['year', 'month', 'amount']

class PaymentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonthlyPayment.objects.all()
    serializer_class = PaymentSerializer
