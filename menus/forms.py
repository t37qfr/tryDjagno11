from django import forms

#models
from .models import Item

#for quryset
from restaurants.models import RestaurantLocation



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public'
        ]

    def __init__(self,user=None,*args,**kwargs):
        #restrict the list of restaurants only for the USER related ones
        super(ItemForm,self).__init__(*args,**kwargs)
       # print(kwargs.pop('instance'))
        self.fields['restaurant'].queryset = RestaurantLocation.objects.filter(owner=user) #.exclude(item__isnull=False)
