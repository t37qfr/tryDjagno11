from django.contrib import admin

#Import the model before add to ADMIN
from .models import Item

admin.site.register(Item)