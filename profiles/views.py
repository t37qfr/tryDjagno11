from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import DetailView, View
# Create your views here.
from menus.models import Item
from restaurants.models import RestaurantLocation

from .models import Profile

User = get_user_model()


class ProfileFollowToggle(LoginRequiredMixin,View):
    def post(self,request,*args,**kwargs):
        user_to_toggle = request.POST.get("username")
        print(user_to_toggle)
        profile_ = Profile.objects.get(user__username__iexact=user_to_toggle)
        user = request.user
        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)

        return redirect('/u/gabor/')

class ProfileDetailView(DetailView):
    template_name='profiles/user.html'

    def get_object(self):
        #get the usernem form kwargs
        username=self.kwargs.get('username')
        #if no username raise 404 error
        if username is None:
            raise Http404
        return get_object_or_404(User,username__iexact=username,is_active=True)

    def get_context_data(self,*args,**kwargs):
        context = super(ProfileDetailView,self).get_context_data(*args,**kwargs)
        user = self.get_object()
        query = self.request.GET.get('q')
        items_exists = Item.objects.filter(user=user).exists()

        qs=RestaurantLocation.objects.filter(owner=user).search(query)

        if qs.exists() and items_exists:
            context['locations']=qs
        return context


