from django.db import models
from developer.models import Developer

# Create your models here.


class Education(models.Model):
    developer = models.ForeignKey(Developer, related_name='education', on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=200)
    _from = models.DateField(blank=True, null=True)
    to = models.DateField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
