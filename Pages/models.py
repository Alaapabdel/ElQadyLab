from django.db import models

# Create your models here.
class Service(models.Model):
    serviceTitle= models.CharField(max_length=100)
    serviceTitleAR= models.CharField(max_length=100)
    serviceBody= models.TextField(max_length=3000)
    serviceBodyAR= models.TextField(max_length=3000)
    serviceImage = models.ImageField(blank=True)
    def __str__(self):
        return self.serviceTitle

class Option(models.Model):
    optionTitle= models.CharField(max_length=100)
    optionTitleAR= models.CharField(max_length=100)

    optionBody= models.TextField(max_length=1000)
    optionBodyAR= models.TextField(max_length=1000)
    def __str__(self):
        return self.optionTitle

class Discount(models.Model):
    discountTitle= models.TextField(max_length=100)
    discountTitleAR= models.TextField(max_length=100)
    def __str__(self):
        return self.discountTitle