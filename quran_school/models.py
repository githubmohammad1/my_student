from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.PositiveIntegerField()
    registration_date = models.DateField()
    phone_number = models.CharField(max_length=20,)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'quran_school'
        ordering = ['name']  # ترتيب الطلاب أبجديًا

    def __str__(self):
        return self.name


class Test(models.Model):
    STUDENT_GRADES = [
        ('جيد', 'جيد'),
        ('جيد جدًا', 'جيد جدًا'),
        ('ممتاز', 'ممتاز'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='tests')
    part_number = models.PositiveIntegerField()
    grade = models.CharField(max_length=10, choices=STUDENT_GRADES)
    date = models.DateField()
    note = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'quran_school'
        ordering = ['-date']

    def __str__(self):
        return f'{self.student.name} - جزء {self.part_number}'


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    day_name = models.CharField(max_length=20)

    class Meta:
        app_label = 'quran_school'
        ordering = ['-date']
        unique_together = ('student', 'date')

    def __str__(self):
        return f'{self.student.name} - {self.date}'


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'quran_school'
        ordering = ['-date']

    def __str__(self):
        return self.title


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    is_paid = models.BooleanField(default=True)

    class Meta:
        app_label = 'quran_school'
        ordering = ['-date']

    def __str__(self):
        return f'{self.student.name} - {self.amount} - {self.date}'


class Progress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='progress_records')
    date = models.DateField()
    pages_listened = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 11)],
        default=1,
        help_text="عدد الصفحات المسموعة (1 – 10)"
    )

    class Meta:
        app_label = 'quran_school'
        unique_together = ('student', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.student.name} – {self.date}: {self.pages_listened} صفحة"
