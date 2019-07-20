from django.db import models
from colorful.fields import RGBColorField
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:100]

class Setting(models.Model):
    title = models.CharField(max_length=20)
    color = RGBColorField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

