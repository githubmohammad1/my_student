from django.db import models

class Person(models.Model):
    ROLE_CHOICES = [
        ('student', 'طالب'),
        ('teacher', 'أستاذ'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    # حقل خاص للأساتذة فقط
    specialization = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_role_display()})"


class QuranPartTest(models.Model):
    GRADE_CHOICES = [
        ('جيد', 'جيد'),
        ('جيد جداً', 'جيد جداً'),
        ('ممتاز', 'ممتاز')
    ]
    student = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='quran_tests_as_student',
        limit_choices_to={'role': 'student'}
    )
    teacher = models.ForeignKey(
        Person,
        on_delete=models.SET_NULL,
        null=True,
        related_name='quran_tests_as_teacher',
        limit_choices_to={'role': 'teacher'}
    )
    part_number = models.PositiveSmallIntegerField()
    date = models.DateField()
    grade = models.CharField(max_length=10, choices=GRADE_CHOICES)

    def __str__(self):
        return f"اختبار جزء {self.part_number} - {self.student}"


class MemorizationSession(models.Model):
    GRADE_CHOICES = [
        ('جيد', 'جيد'),
        ('جيد جداً', 'جيد جداً'),
        ('ممتاز', 'ممتاز')
    ]
    student = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='memorization_sessions_as_student',
        limit_choices_to={'role': 'student'}
    )
    teacher = models.ForeignKey(
        Person,
        on_delete=models.SET_NULL,
        null=True,
        related_name='memorization_sessions_as_teacher',
        limit_choices_to={'role': 'teacher'}
    )
    page_number = models.PositiveSmallIntegerField()
    date = models.DateField()
    grade = models.CharField(max_length=10, choices=GRADE_CHOICES)

    def __str__(self):
        return f"تسميع صفحة {self.page_number} - {self.student}"


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('حاضر', 'حاضر'),
        ('غائب', 'غائب')
    ]
    SESSION_CHOICES = [
        ('صباح', 'صباح'),
        ('مساء', 'مساء')
    ]
    student = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='attendance_records',
        limit_choices_to={'role': 'student'}
    )
    date = models.DateField()
    session_time = models.CharField(max_length=10, choices=SESSION_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student} - {self.date} ({self.session_time})"
from django.db import models

class MemorizedPage(models.Model):
    GRADE_CHOICES = [
        ('جيد', 'جيد'),
        ('جيد جداً', 'جيد جداً'),
        ('ممتاز', 'ممتاز'),
    ]

    student = models.ForeignKey('Person', on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    page_number = models.PositiveIntegerField()
    grade = models.CharField(max_length=20, choices=GRADE_CHOICES)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'page_number', 'date')

    def __str__(self):
        return f"{self.student} - صفحة {self.page_number} - {self.grade}"
