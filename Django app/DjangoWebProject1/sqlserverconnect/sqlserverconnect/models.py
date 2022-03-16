from django.db import models
import pyodbc

class sqlserver(models.Model):
    Empname = models.CharField()