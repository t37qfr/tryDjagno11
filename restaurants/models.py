#for user model = ForignKey
from django.conf import settings

from django.db import models
#signals for slug
from django.db.models.signals import pre_save,post_save
#Elminate hard coded url path
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator

from .validators import validate_category

from django.db.models  import Q

# Create your models here.
'''
Add RESTAURANTS to the INSTALLED APPS
-null DB can be empty
-blank Field in admin and form can be empty
'''

User = settings.AUTH_USER_MODEL


class RestaurantLocationQuerySet(models.query.QuerySet):
    def search(self,query):
        if query:
            query=query.strip()
            return self.filter(
                Q(name__icontains=query)|
                Q(location__icontains=query)|
                Q(category__icontains=query)|
                Q(item__name__icontains=query)
            ).distinct()
        return self

class RestaurantLocationManager(models.Manager):
    def get_queryset(self):
        return RestaurantLocationQuerySet(self.model, using=self._db)
    def search(self,query):
        return self.get_queryset().search(query)

class RestaurantLocation(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True,blank=True)
    category = models.CharField(max_length=120, null=True,blank=True,validators=[validate_category])
    timestamp = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    my_date_field=models.DateField(auto_now_add=False,auto_now=False,null=True,blank=True)
    slug = models.SlugField( null=True,blank=True)

    objects = RestaurantLocationManager() #add Model.objects.all()

    def __str__(self):
        return self.name

    '''redirect from the ListView to the proper place'''
    def get_absolute_url(self):
       # return f"/restaurants/{self.slug}"
        return reverse('restaurants:detail',kwargs={'slug':self.slug})

    @property
    def title(self):
        return self.name


def rl_pre_save_receiver(sender,instance,*args,**kwargs):
    '''do not have to call instance.save()'''
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

# def rl_post_save_receiver(sender,instance,created,*args,**kwargs):
#     '''need to call .save() but only in a loop with condation (avoid infinite loop'''
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()


pre_save.connect(rl_pre_save_receiver,sender=RestaurantLocation)
#post_save.connect(rl_post_save_receiver,sender=RestaurantLocation)


