from django.db import models
from classrooms.models import ClassRoom
from teachers.models import Teacher

class Subject(models.Model):
    name = models.CharField(max_length=100)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} ({self.class_room})"
