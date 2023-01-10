from django.db import models

# Create your models here.
class Input(models.Model):
    content = models.TextField(max_length=9999, unique=True,)
    character_length = models.CharField(max_length=4)

class Session(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    session_key = models.CharField(max_length=50, unique=True,)
    inputs = models.ManyToManyField(Input)

class Translation(models.Model):
    language = models.CharField(max_length=15,)
    input = models.ForeignKey(Input, on_delete=models.CASCADE)
    output = models.TextField(max_length=999999999, default="")
