from django.shortcuts import render, get_object_or_404
#Class Based view
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView,CreateView

from django.http import HttpResponse,HttpResponseRedirect

#for DB connection
from .models import RestaurantLocation
#form
from .forms import RestaurantCreateForm, RestorantLocationCreateForm

#Q query lookup
from django.db.models import Q

def restaurant_listview(request):
    #template_name='restaurants/restaurantlocation_list.html'
    queryset=RestaurantLocation.objects.all()
    context={
        'object_list':queryset
    }
    return render(request,template_name,context)


def restaurant_createview(request):
    form = RestorantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/restaurants/")
    if form.errors:
        errors=form.errors

    template_name = 'restaurants/form.html'
    context = {'form':form,'errors':errors}
    return render(request, template_name, context)


'''
Class based view
'''
#List view
class RestaurantListView(ListView):
    '''template renamed for basic name: restaurantlocation_list.html'''
    #template_name = 'restaurants/restaurantlocation_list.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) | Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


#detail view
class RestaurantDetailView(DetailView):
    template_name = 'restaurants/restaurantlocation_detail.html'
    queryset = RestaurantLocation.objects.all()


class RestaurantCreateView(CreateView):
    form_class = RestorantLocationCreateForm
    template_name = 'restaurants/form.html'
    success_url = "/restaurants/"

