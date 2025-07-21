from django.contrib import admin
from .models import ClassRoom

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'section')
    list_filter = ('name', 'section')
    search_fields = ('name', 'section')
