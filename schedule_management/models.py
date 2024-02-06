from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Grade(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING)
    def __str__(self) :
        return f"{self.name} {self.surname}"