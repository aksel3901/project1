from django.db import models

# Create your models here.
class StudentUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.PositiveIntegerField(primary_key=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    grad_year = models.IntegerField()
    
class Campus(models.Model):
    pass
class Course(models.Model):
    pass
