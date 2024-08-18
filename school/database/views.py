from django.shortcuts import render
from django.views.generic import ListView
from database import models

# Create your views here.
class StudentsListView(ListView):
    model = models.Student
    context_object_name = "students"
    template_name = "database/students-list.html"


def teacher_list(request):
    teachers = models.Teacher.objects.all()
    context = {
        "teachers": teachers
    }
    
    return render(request, "database/teachers-list.html", context)