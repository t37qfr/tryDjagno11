from django.utils.text import slugify
#for random generator
import random
import string


DONT_USE=['create']

'''Unique SLUG generator'''
def unique_slug_generator(instance,new_slug=None):
    '''
    For Django: assumes your instance has a model with slug field and
    a title charcter (char) field
    '''
    if new_slug is not None:
        slug=new_slug
    else:
        slug=slugify(instance.title)

    if slug in DONT_USE:
        new_slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug=new_slug)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(slug=slug,randstr=random_string_generator(size=4))
        return unique_slug_generator(instance,new_slug=new_slug)
    return slug

'''Random string generator'''
def random_string_generator(size=10,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))




