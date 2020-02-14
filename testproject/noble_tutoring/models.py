from django.db import models

# Create your models here.
class StudentUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.PositiveIntegerField(primary_key=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    grad_year = models.IntegerField()
    campus = models.ForeignKey('Campus', on_delete=models.CASCADE)

class Campus(models.Model):
    name = models.CharField()

    # logo_picture =

class Course(models.Model):
    name = models.CharField()

    pass
