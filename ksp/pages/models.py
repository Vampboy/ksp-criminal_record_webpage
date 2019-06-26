from django.db import models

# Create your models here.
class criminal(models.Model):
    criminal_name = models.CharField(max_length=50) 
    criminal_Img = models.ImageField(upload_to='ksp/static/images/')