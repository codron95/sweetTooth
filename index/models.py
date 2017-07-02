from django.db import models

foodTypes = (('IC','Ice Cream'),
	('CK','Cakes'),
	('SW','Sweets'),
	)

class foodItem(models.Model):
	name = models.CharField(max_length=20,blank=False,null=False)
	foodType = models.CharField(max_length=20,blank=False,null=False,choices=foodTypes,default = 'IC')
	desc = models.CharField(max_length=255,blank=True,null=False)
	price = models.FloatField(null=False,default = 0)
	image = models.ImageField(upload_to="images/",default = "images/default.jpg")

	def __str__(self):
		return self.name


