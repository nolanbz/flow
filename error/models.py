from django.db import models

class Issue(models.Model):

    timestamp	= models.DateTimeField(auto_now=True, auto_now_add=False)
    updated		= models.DateTimeField(auto_now=False, auto_now_add=True)
    image		= models.FileField(null=True, blank=True, default='/placeholder.png')

    title       = models.CharField(max_length=120)
    body        = models.TextField()
    location    = models.CharField(max_length=120)
		
    class Meta:
	    ordering = ["-timestamp", "-updated"]
