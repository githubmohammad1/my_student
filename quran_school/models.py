from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    STATUS_CHOICES = [
        ('active', 'نشط'),
        ('paused', 'موقوف مؤقتًا'),
        ('graduated', 'متخرج'),
    ]

    name = models.CharField('اسم الطالب', max_length=100)
    father_name = models.CharField('اسم الأب', max_length=100, null=True, blank=True)
    age = models.PositiveSmallIntegerField('العمر', validators=[MinValueValidator(3), MaxValueValidator(99)])
    current_grade = models.CharField('الصف الدراسي', max_length=20)
    passed_juz = models.PositiveSmallIntegerField('كم جزءًا يحفظ', default=0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    whatsapp = models.CharField('رقم الواتس', max_length=20)
    nearest_address = models.TextField('أقرب عنوان', null=True, blank=True)
    registration_date = models.DateField('تاريخ التسجيل')
    status = models.CharField('الحالة', max_length=10, choices=STATUS_CHOICES, default='active')

    class Meta:
        app_label = 'quran_school'
        ordering = ['name']
        verbose_name = 'طالب'
        verbose_name_plural = 'الطلاب'

    def __str__(self):
        return self.name


class Test(models.Model):
    GRADE_CHOICES = [
        ('جيد', 'جيد'),
        ('جيد جدًا', 'جيد جدًا'),
        ('ممتاز', 'ممتاز'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='tests', verbose_name='الطالب')
    part_number = models.PositiveSmallIntegerField('الجزء', validators=[MinValueValidator(1), MaxValueValidator(30)])
    grade = models.CharField('التقدير', max_length=10, choices=GRADE_CHOICES)
    date = models.DateField('التاريخ', db_index=True)
    note = models.TextField('ملاحظة', null=True, blank=True)

    class Meta:
        app_label = 'quran_school'
        ordering = ['-date']
        verbose_name = 'اختبار'
        verbose_name_plural = 'الاختبارات'

    def __str__(self):
        return f'{self.student.name} - جزء {self.part_number}'


class MonthlyPayment(models.Model):
    MONTH_CHOICES = [(m, str(m)) for m in range(1, 13)]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments', verbose_name='الطالب')
    amount = models.DecimalField('المبلغ المودَع', max_digits=8, decimal_places=2)
    month = models.PositiveSmallIntegerField('رقم الشهر', choices=MONTH_CHOICES)
    year = models.PositiveSmallIntegerField('العام', validators=[MinValueValidator(2020), MaxValueValidator(2100)])
    is_paid = models.BooleanField('مدفوع', default=True)

    class Meta:
        app_label = 'quran_school'
        ordering = ['-year', '-month']
        unique_together = ('student', 'month', 'year')
        verbose_name = 'دفعة شهرية'
        verbose_name_plural = 'الدفعات الشهرية'

    def __str__(self):
        return f'{self.student.name} - {self.amount} - {self.month}/{self.year}'


class Announcement(models.Model):
    content = models.TextField('الإعلان')
    created_at = models.DateTimeField('تاريخ النشر', auto_now_add=True)
    date = models.DateField(auto_now_add=True)


    class Meta:
        app_label = 'quran_school'
        ordering = ['-created_at']
        verbose_name = 'إعلان'
        verbose_name_plural = 'الإعلانات'

    def __str__(self):
        return (self.content[:50] + '...') if len(self.content) > 50 else self.content


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Attendance(models.Model):
    PERIOD_CHOICES = [
        ('morning', 'صباحًا'),
        ('evening', 'مساءً'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='attendances',
        verbose_name='الطالب'
    )
    date = models.DateField('التاريخ', db_index=True)

    period = models.CharField(
        'الفترة',
        max_length=50,
        choices=PERIOD_CHOICES,
        default='evening'
    )

    present = models.BooleanField('الحضور', default=True)

    # عدد الصفحات المسموعة
    pages_listened = models.PositiveSmallIntegerField(
        'عدد الصفحات المسموعة',
        validators=[MinValueValidator(0), MaxValueValidator(20)],
        null=True, blank=True,
        help_text="عدد الصفحات المسموعة (0 – 20)"
    )

    # ملاحظة لرقم الصفحة من المصحف
    page_note = models.CharField(
        'رقم الصفحة من المصحف',
        max_length=10,
        null=True, blank=True,
        help_text="اكتب رقم الصفحة من المصحف هنا"
    )

    tested = models.BooleanField('هل اختبر', default=False)
    test = models.ForeignKey(
        Test,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='رابط الاختبار'
    )

    class Meta:
        app_label = 'quran_school'
        ordering = ['-date', 'student__name', 'period']
        unique_together = ('student', 'date', 'period')
        verbose_name = 'حضور'
        verbose_name_plural = 'الحضور'

    def __str__(self):
        return f'{self.student.name} - {self.date} ({self.get_period_display()})'
