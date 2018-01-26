from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User) # user.profile
    followers = models.ManyToManyField(User,related_name='is_following',blank=True) # user.followers.all()
    #Do not need this : prev. ManyToManyField cover this
    #following = models.ManyToManyField(User,related_name='following',blank=True) # user.following.all()
    activated = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def post_save_user_receiver(sender,instance,created,*arg,**kwargs):
        if created:
            profile, is_created = Profile.objects.get_or_create(user=instance)
            default_user_profile = Profile.objects.get(user__id=1)[0]
            default_user_profile.followers.add(instance)
            #default_user_profile.save() #Do not have to do that
            #follow back
            profile.followers.add(default_user_profile)

    post_save.connect(post_save_user_receiver,sender=User)
