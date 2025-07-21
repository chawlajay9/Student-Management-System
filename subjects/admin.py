from django.contrib import admin
from .models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_room', 'teacher')
    list_filter = ('class_room', 'teacher')
    search_fields = ('name',)
