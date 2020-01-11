from django.db import models

# Create your models here.
class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'data_images')
    desc = models.TextField()
    price = models.IntegerField()
    special_offer = models.BooleanField(default=False)