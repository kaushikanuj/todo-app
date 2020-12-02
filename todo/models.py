from django.db import models


# Create your models here.
class TodoApp(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
