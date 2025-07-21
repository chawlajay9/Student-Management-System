from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_id', 'hire_date')
    list_filter = ('hire_date',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'employee_id')
