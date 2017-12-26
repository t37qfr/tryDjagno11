from django.shortcuts import render
#Class Based view
from django.views import View
from django.views.generic import TemplateView

#for DB connection
from .models import RestaurantLocation

def restaurant_listview(request):
    template_name='restaurants/restaurant_list.html'
    queryset=RestaurantLocation.objects.all()
    context={
        'object_list':queryset
    }
    return render(request,template_name,context)



'''
Class based view
'''
# class AboutView(TemplateView):
#     template_name = 'home2.html'
#
# class ContactView(TemplateView):
#     template_name = 'home3.html'