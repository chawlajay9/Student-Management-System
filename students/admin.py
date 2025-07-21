from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id', 'admission_date', 'class_assigned', 'section')
    list_filter = ('admission_date', 'class_assigned', 'section')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'student_id')
