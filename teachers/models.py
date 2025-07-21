from django.db import models
from users.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    hire_date = models.DateField()

    def __str__(self):
        return self.user.get_full_name()
