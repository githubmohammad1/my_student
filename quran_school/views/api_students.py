# quran_school/views/api_students.py
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Student
from ..serializers import StudentSerializer
from rest_framework import permissions
class StudentListCreateAPI(generics.ListCreateAPIView):
    """
    API لعرض كل الطلاب أو إنشاء طالب جديد
    مع دعم الفلترة والبحث والترتيب.
    """
    def get_permissions(self):

        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # فلترة حسب الحقول
    filterset_fields = ['status', 'current_grade']
    
    # البحث في هذه الحقول
    search_fields = ['name', 'father_name', 'whatsapp']
    
    # الترتيب حسب هذه الحقول
    ordering_fields = ['name', 'registration_date']


class StudentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    API لجلب أو تعديل أو حذف طالب معيّن باستخدام الـ pk
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
