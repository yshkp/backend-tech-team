from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^$', views.land, name="land"),
    url(r'^home/$', views.home, name="home"),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^login/$', auth_views.login, { 'template_name': 'bellybean/login.html' }, name='login'),
    url(r'^logout/$', auth_views.logout, { 'template_name': 'bellybean/logout.html', 'next_page': reverse_lazy('land') }, name='logout'),
    url(r'^select_area/$', views.select_area, name='select_area'),
    url(r'^registerrest/$', views.RegisterRestaurant.as_view(), name='registerrest'),
    url(r'^selectrest/$', views.selectrest, name="selectrest"),
    url(r'^(?P<rest_id>[0-9]+)/$', views.RegisterDishes.as_view(), name='registerdishes'),
    url(r'^(?P<area>[a-zA-Z]+)/$', views.selectresttoorder, name='selectresttoorder'),
    url(r'^(?P<area>[a-zA-Z]+)/(?P<rest_id>[0-9]+)/$', views.select_dish, name='selectdish'),

]