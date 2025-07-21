from django.db import models

class ClassRoom(models.Model):
    name = models.CharField(max_length=20)  # e.g. "Class 1"
    section = models.CharField(max_length=1)  # A, B, C

    class Meta:
        unique_together = ('name', 'section')

    def __str__(self):
        return f"{self.name} - {self.section}"
