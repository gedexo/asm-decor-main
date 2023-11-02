from django.db import models
from django.utils.text import slugify
# Create your models here.



class ServiceCategory(models.Model):
    name=models.CharField(max_length=30)
    icon=models.ImageField()
    description=models.TextField()
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Service (models.Model):
    category=models.ForeignKey("web.ServiceCategory",on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    image=models.ImageField()
    description=models.TextField()
    slug = models.SlugField(unique=True, max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.title)



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

    
class ServiceEnquiry(models.Model):
    service = models.ForeignKey("web.Service", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Update(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    date=models.DateField()
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title