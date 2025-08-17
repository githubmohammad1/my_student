from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from ..models import Attendance
from ..serializers import ProgressSerializer

class ProgressListCreateAPI(generics.ListCreateAPIView):
    queryset = Attendance.objects.all().order_by('-date')
    serializer_class = ProgressSerializer

class ProgressDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = ProgressSerializer

class ProgressReportAPI(APIView):
    """
    API لإرجاع إحصائيات تقدم الطلاب مع فلترة متقدمة
    """
    def get(self, request):
        student_id = request.GET.get('student_id')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        period = request.GET.get('period')

        qs = Attendance.objects.all()
        if student_id:
            qs = qs.filter(student_id=student_id)
        if start_date:
            qs = qs.filter(date__gte=start_date)
        if end_date:
            qs = qs.filter(date__lte=end_date)
        if period:
            qs = qs.filter(period=period)

        total_pages = qs.aggregate(total=Sum('pages_listened'))['total'] or 0
        total_tests = qs.filter(tested=True).count()

        return Response({
            "total_pages_listened": total_pages,
            "total_tests_done": total_tests,
            "records_count": qs.count(),
            "filters_used": {
                "student_id": student_id,
                "start_date": start_date,
                "end_date": end_date,
                "period": period,
            }
        })
