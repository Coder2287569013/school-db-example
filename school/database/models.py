from django.db import models
from sortedm2m.fields import SortedManyToManyField

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Grade(models.Model):
    name = models.CharField(max_length=5)
    head_teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    subjects = SortedManyToManyField("Subject", related_name="subjects")

    def __str__(self):
        return f'''Name: {self.name},
        Head Teacher: {self.head_teacher}, 
        Subjects: {self.subjects.all()}'''
    

class Student(models.Model):
    name = models.CharField(max_length=255)
    grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Name: {self.name}, Grade: {Grade.objects.get(id=self.grade_id).name}"
