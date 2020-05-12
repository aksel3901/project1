from django.shortcuts import render, redirect

from django.shortcuts import get_object_or_404
# from django.http import HttpResponse

from .models import *


def index(request):
    all_courses = Course.objects.all()
    context = {'all_courses': all_courses, }
    return render(request, 'noble_tutoring/index.html', context)


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {'course': course, }
    return render(request, 'noble_tutoring/course.html', context)
    # return HttpResponse("You're looking at course %s" % course_id)


def homepage_view(request):
    return render(request, 'noble_tutoring/homepage.html')


def login_page(request):
    return render(request, 'noble_tutoring/login_page.html')


def register_page(request):
    return render(request, 'noble_tutoring/register_page.html')


def login_user(request):
    if request.method == "POST":
        user = StudentUser.objects.get(email=request.POST['email'])
    return redirect("/tutoring/profile_page")

def profile_page(request):
    return render(request, 'noble_tutoring/profile_page.html')
