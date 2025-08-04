from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(null=True, max_length=100)
    mother_name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField()
    registration_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return self.name


class Test(models.Model):
    STUDENT_GRADES = [
        ('جيد', 'جيد'),
        ('جيد جدًا', 'جيد جدًا'),
        ('ممتاز', 'ممتاز'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    part_number = models.PositiveIntegerField()
    grade = models.CharField(max_length=10, choices=STUDENT_GRADES)
    date = models.DateField()
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.student.name} - جزء {self.part_number}'


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='attendances')
    # related_name='attendances'           adding 
    date = models.DateField()
    day_name = models.CharField(max_length=20)
    # memorized_pages = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.student.name} - {self.date}'


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ✅ تعديل الاسم من StudentFund إلى Payment
class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')  # ✅ إضافة related_name
    amount = models.DecimalField(max_digits=8, decimal_places=2)  # ✅ تغيير النوع إلى DecimalField
    date = models.DateField()
    is_paid = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.student.name} - {self.amount} - {self.date}'
# quran_school/models.py

from django.db import models

class Progress(models.Model):
    student          = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='progress_records'
    )
    date             = models.DateField()
    pages_listened   = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        default=1,
        help_text="عدد الصفحات المسموعة (1 – 5)"
    )

    class Meta:
        unique_together = ('student', 'date')
        ordering        = ['-date']

    def __str__(self):
        return f"{self.student.name} – {self.date}: {self.pages_listened} صفحة"
