from django.db import models
#signals for slug
from django.db.models.signals import pre_save,post_save

from .utils import unique_slug_generator

# Create your models here.
'''
Add RESTAURANTS to the INSTALLED APPS
-null DB can be empty
-blank Field in admin and form can be empty
'''
class RestaurantLocation(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True,blank=True)
    category = models.CharField(max_length=120, null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    my_date_field=models.DateField(auto_now_add=False,auto_now=False,null=True,blank=True)
    slug = models.SlugField( null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


def rl_pre_save_receiver(sender,instance,*args,**kwargs):
    '''do not have to call instance.save()'''
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

# def rl_post_save_receiver(sender,instance,created,*args,**kwargs):
#     '''need to call .save() but only in a loop with condation (avoid infinite loop'''
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()


pre_save.connect(rl_pre_save_receiver,sender=RestaurantLocation)
#post_save.connect(rl_post_save_receiver,sender=RestaurantLocation)


