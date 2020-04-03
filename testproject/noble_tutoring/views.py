from django.shortcuts import render

from django.shortcuts import get_object_or_404
# from django.http import HttpResponse

from .models import Course

def index(request):
    all_courses = Course.objects.all()
    context = {'all_courses' : all_courses, }
    return render(request, 'noble_tutoring/index.html', context)

def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {'course' : course, }
    return render(request, 'noble_tutoring/course.html', context)
    # return HttpResponse("You're looking at course %s" % course_id)