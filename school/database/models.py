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
        return f"{self.name}, {self.subject}"

class Grade(models.Model):
    name = models.CharField(max_length=5)
    head_teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    subjects = models.ManyToManyField("Subject")

    def __str__(self):
        return f"{self.name}, {self.head_teacher}"

class Student(models.Model):
    name = models.CharField(max_length=255)
    grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}, {Grade.objects.get(id=self.grade).name}"
