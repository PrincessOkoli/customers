from django.db import models

# Create your models here.
class customers(models.Model):
    first_name = models.CharField(max_length = 100, blank = True)
    Last_name = models.CharField(max_length = 100)
    age = models.CharField(max_length = 50, default="00") 
    phone = models.IntegerField()
    # go on your commandline and migrate your code


    def __str__(self):
        return self.first_name + " " + self.Last_name
