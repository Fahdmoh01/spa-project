from django.db import models

# Create your models here.
class Staff(models.Model):
	name= models.CharField(max_length=255)
	phone= models.CharField(max_length=15, default="0505757031")
	position = models.CharField(max_length=255)
	image = models.ImageField(upload_to="staff/")
	description = models.TextField()
	
	def __str__(self):
		return self.name
	