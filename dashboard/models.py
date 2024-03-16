from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) 
    description = models.TextField()

    class Meta:
        verbose_name = "notes"  
        verbose_name_plural = "notes"

    #if you want to see the tittle name an database
    def __str__(self):
        return self.title
