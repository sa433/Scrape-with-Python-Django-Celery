from django.db import models

# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    plink = models.CharField(max_length=1000)


