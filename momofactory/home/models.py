from django.db import models
from django.db.models.fields import IntegerField, TextField
from django.utils import text
from django.utils.text import slugify
import jsonfield

# Create your models here.

class Popular(models.Model):
    title=models.CharField(max_length=255)
    img=models.ImageField(upload_to='image')
    description=models.TextField()
    price1=models.IntegerField(default=0)
    price2=models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    name=models.CharField(max_length=255)
    position=models.CharField(max_length=255)
    img=models.ImageField(upload_to='image')
    description=models.TextField()
    stars=models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=50)
    img=models.ImageField(upload_to='image')

class News(models.Model):
    title=models.TextField()
    writer=models.CharField(max_length=255)
    date=models.DateField()
    img=models.ImageField(upload_to='image')
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()

    def __str__(self):
        return self.title
    