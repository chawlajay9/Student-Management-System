from django.db import models
from classrooms.models import ClassRoom
from subjects.models import Subject
from students.models import Student

class Exam(models.Model):
    name = models.CharField(max_length=50)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.class_room}"

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        unique_together = ('student', 'subject', 'exam')

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.exam}: {self.score}"
