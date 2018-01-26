from django.conf import settings
from django.db import models

from restaurants.models import RestaurantLocation

#Elminate hard coded url path
from django.core.urlresolvers import reverse

'''
Before Migration: add the APP to the INSTALLED_APPS list!!!
'''

class Item(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant      = models.ForeignKey(RestaurantLocation)
    #itme stuff
    name            = models.CharField(max_length=120)
    contents        = models.TextField(help_text='separete by comma')
    excludes         = models.TextField(blank=True, null=True, help_text='separete by comma')
    public          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    '''redirect from the ListView to the proper place'''
    def get_absolute_url(self):
        return reverse('menus:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-updated','-timestamp'] #most recently updated Item.objects.all()


    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")