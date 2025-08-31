from django.contrib import admin
from .models import Person, QuranPartTest, MemorizationSession, Attendance
from .models import MemorizedPage
admin.site.register(Person)
admin.site.register(QuranPartTest)
admin.site.register(MemorizationSession)
admin.site.register(Attendance)

@admin.register(MemorizedPage)
class MemorizedPageAdmin(admin.ModelAdmin):
    list_display = ('student', 'page_number', 'grade', 'date')
    list_filter = ('grade', 'date')