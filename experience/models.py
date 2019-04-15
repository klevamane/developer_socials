from django.db import models
from developer.models import Developer

# Create your models here.


class Experience(models.Model):
    developer = models.ForeignKey(Developer, related_name='experiences', on_delete=models.CASCADE)

    organization = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    _from = models.DateField()
    to = models.DateField(blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
