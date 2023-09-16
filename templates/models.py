from django.db import models

class Template(models.Model):
	title 				= models.CharField(max_length=40, null=False, blank=True)
	body 				= models.TextField(max_length=150, null=False, blank=True)
	created 		= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	updated 		= models.DateTimeField(auto_now=True, verbose_name="date updated")

	def __str__(self):
		return self.title