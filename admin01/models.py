from django.db import models

# Create your models here.

class EmpList(models.Model):
    name = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)
    age = models.IntegerField()
    headpic = models.ImageField(upload_to='pic')

    class Meta:
        db_table= 'emplist'