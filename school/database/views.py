from django.shortcuts import render
from django.views.generic import ListView
from database import models

# Create your views here.
class StudentsListView(ListView):
    model = models.Student
    context_object_name = "students"
    template_name = "students-list.html"