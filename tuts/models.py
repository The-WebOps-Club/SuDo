from django.db import models

# Create your models here.

class Tutsheet(models.Model):
	filename = models.FileField(upload_to='media/tuts')
	verbose_name = models.CharField(max_length = 50)
