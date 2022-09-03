from distutils.command.upload import upload
from django.db import models
from numpy import maximum

class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100, null=False)
    def __str__(self) -> str:
        return str(self.id)+" "+self.name

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    def __str__(self) -> str:
        return str(self.id) + " " + self.name

# Create your models here.
class Employee(models.Model):    
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30,null = False)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
    
    def __str__(self) -> str:
        return str(self.id)+" " + self.first_name + " " + self.last_name + " " + self.dept.name + " " + self.role.name