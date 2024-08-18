from django.db import models
from sortedm2m.fields import SortedManyToManyField

# Create your models here.
from django.db import models

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
    class_teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'''{self.name},
        Class Teacher: {self.class_teacher}'''
    

class Student(models.Model):
    name = models.CharField(max_length=255)
    grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Name: {self.name}, Grade: {Grade.objects.get(id=self.grade_id).name}"


class Schedule(models.Model):
    order = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order}, {self.subject}, {self.grade}"

class Score(models.Model):
    score = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student}, {self.subject}, {self.score}"
