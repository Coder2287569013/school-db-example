from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
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


def student_details(request, pk):
    try:
        student = models.Student.objects.get(id=pk)
    except models.Student.DoesNotExist:
        HttpResponse("Student doesn't exist", status=404)
 
    context = {
        "student_info": student
    }

    return render(request, "database/student-details.html", context)
