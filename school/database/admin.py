from django.contrib import admin
from .models import Subject, Teacher, Grade, Student

# Register your models here.
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Grade)
admin.site.register(Student)