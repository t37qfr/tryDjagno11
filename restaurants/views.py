#login decorator
from django.contrib.auth.decorators import login_required
#login require for class based view
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
#Class Based view
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView,CreateView,UpdateView

from django.http import HttpResponse,HttpResponseRedirect

#for DB connection
from .models import RestaurantLocation
#form
from .forms import RestaurantCreateForm, RestorantLocationCreateForm

#Q query lookup
from django.db.models import Q



'''
Class based view
'''
#List view
class RestaurantListView(LoginRequiredMixin,ListView):
    '''template renamed for basic name: restaurantlocation_list.html'''
    #template_name = 'restaurants/restaurantlocation_list.html'

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)


#detail view
class RestaurantDetailView(DetailView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestorantLocationCreateForm
    login_url = '/login/'
    template_name = 'form.html'
    #success_url = "/restaurants/" : not the best way to do that -> get_absolute_url()

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        #instance.save() /*Do not need, form_valid method do the job*/
        return super(RestaurantCreateView,self).form_valid(form)

    def get_context_data(self, *args,**kwargs):
        context = super(RestaurantCreateView,self).get_context_data(*args,*kwargs)
        context['title']='Add Restaurant'
        return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestorantLocationCreateForm
    login_url = '/login/'
    template_name = 'restaurants/detail-update.html'
    #success_url = "/restaurants/" : not the best way to do that -> get_absolute_url()

    def get_context_data(self, *args,**kwargs):
        context = super(RestaurantUpdateView,self).get_context_data(*args,*kwargs)
        context['title']='Add Restaurant'
        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

