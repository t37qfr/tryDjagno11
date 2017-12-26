from django.db import models


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


