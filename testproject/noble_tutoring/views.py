from django.http import HttpResponse 
from django.template import loader

from .models import Course

def index(request):
    all_courses = Course.objects.all()
    template = loader.get_template('noble_tutoring/index.html')
    context = {'all_courses' : all_courses, }
    return HttpResponse(template.render(context, request))