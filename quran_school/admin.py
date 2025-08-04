from django.contrib import admin
from .models import Student, Test, Attendance, Announcement, Payment,Progress

admin.site.register(Student)
admin.site.register(Test)
admin.site.register(Attendance)
admin.site.register(Announcement)
admin.site.register(Payment)
admin.site.register(Progress)
