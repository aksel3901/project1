from django.shortcuts import render

from .models import Course

def index(request):
    all_courses = Course.objects.all()
    context = {'all_courses' : all_courses, }
    return render(request, 'noble_tutoring/index.html', context)