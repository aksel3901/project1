from django.contrib import admin
from noble_tutoring.models import StudentUser, Campus, Course

# Register your models here.
admin.site.register(StudentUser)
admin.site.register(Campus)
admin.site.register(Course)