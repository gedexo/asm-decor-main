from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class ServiceCategory(models.Model):
    name=models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True)
    image=models.ImageField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "ServiceCategories"  

class Service(models.Model):
    category=models.ForeignKey("web.ServiceCategory",on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    slug = models.SlugField(unique=True, max_length=100, blank=True, null=True)
    image=models.ImageField(upload_to='service')
    description=HTMLField()

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
    
    class Meta:
        verbose_name_plural = "ServiceEnquiries"

class Update(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='update')
    date=models.DateField()
    description = HTMLField()
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title
    

class Career(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    message = models.TextField()
    cv = models.FileField(upload_to='career')

    def __str__(self):
        return self.name
    

class Project(models.Model):
    image = models.ImageField(upload_to="project")
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    review = models.TextField()

    def __str__(self):
        return self.name