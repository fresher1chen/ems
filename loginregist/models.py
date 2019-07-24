from django.db import models

# Create your models here.
class AdminList(models.Model):
    name = models.CharField(max_length=20)
    T_name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    gender = models.CharField(max_length=5)

    class Meta:
        db_table = 'adminlist'