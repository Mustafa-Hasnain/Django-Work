from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title #making a Constructor so it would return project title first

class Students(models.Model):
    std_name = models.CharField(max_length=50)
    std_contact = models.IntegerField()
    std_roll = models.CharField(max_length = 50, default = '')
    project = models.ForeignKey(Project, on_delete= models.CASCADE)

    def __str__(self):
        return self.std_name
