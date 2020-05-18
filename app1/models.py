from django.db import models

# Create your models here.
class Employees(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    emp_id = models.CharField(max_length = 200)

    # def __str__(self):
    #     return self.firstname