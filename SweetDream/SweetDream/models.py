from django.db import models 

class RC(models.Model):
	psdiscord = models.CharField(max_length=2000,blank=True)
	psmc = models.CharField(max_length=2000,blank=True)
	anps = models.CharField(max_length=2000,blank=True)