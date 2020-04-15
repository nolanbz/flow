from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.conf import settings
from django.urls import reverse

User = settings.AUTH_USER_MODEL

class Product(models.Model):

    draft 			= models.BooleanField(default=True)
    owner			= models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp		= models.DateTimeField(auto_now=True, auto_now_add=False)
    updated			= models.DateTimeField(auto_now=False, auto_now_add=True)
    image			= models.FileField(null=True, blank=True, default='/placeholder.png')
    slug 			= models.SlugField(unique=True)

    manufacture     = models.CharField(max_length=120)
    title           = models.CharField(max_length=120)
    star_rating     = models.CharField(max_length=120)
    price           = models.CharField(max_length=120)
    sale_price      = models.CharField(max_length=120)
    shipping        = models.CharField(max_length=120)
    inventory       = models.CharField(max_length=120)
    features        = models.TextField()
    description     = models.TextField()
    dimensions      = models.CharField(max_length=120)
    item_weight     = models.CharField(max_length=120)
    shipping_weight = models.CharField(max_length=120)
    ASIN            = models.CharField(max_length=120)
    model_number    = models.CharField(max_length=120)
    batteries       = models.CharField(max_length=120)
    review_blip     = models.CharField(max_length=120)
    BSR             = models.CharField(max_length=120)
    category        = models.CharField(max_length=120)
		
    class Meta:
	    ordering = ["-timestamp", "-updated"]

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    instance.category = instance.category.lower()

pre_save.connect(pre_save_post_receiver, sender=Product)
    
    


    
