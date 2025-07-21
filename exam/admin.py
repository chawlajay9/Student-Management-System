from django.contrib import admin
from .models import Exam, Mark

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_room', 'date')
    list_filter = ('class_room', 'date')
    search_fields = ('name',)

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'exam', 'score')
    list_filter = ('exam', 'subject')
    search_fields = ('student__user__username', 'student__user__first_name', 'student__user__last_name')
