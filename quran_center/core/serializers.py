from rest_framework import serializers
from .models import Person, QuranPartTest, MemorizationSession, Attendance

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

from rest_framework import serializers
from .models import MemorizedPage

class MemorizedPageSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.first_name', read_only=True)

    class Meta:
        model = MemorizedPage
        fields = '__all__'

class QuranPartTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuranPartTest
        fields = '__all__'


class MemorizationSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemorizationSession
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
