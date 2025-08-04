# quran_school/api/serializers.py
from rest_framework import serializers
from quran_school.models import Progress

# quran_school/api/serializers.py

class ProgressSerializer(serializers.ModelSerializer):
    student_name    = serializers.CharField(source='student.name', read_only=True)

    class Meta:
        model  = Progress
        fields = [
            'id',
            'student', 
            'student_name',
            'date',
            'pages_listened',
        ]
