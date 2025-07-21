from django.db import models
from users.models import User
from classrooms.models import ClassRoom

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    admission_date = models.DateField()
    class_assigned = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)
    section = models.CharField(max_length=1)

    def __str__(self):
        return self.user.get_full_name()
