from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^$', views.land, name="land"),
    url(r'^home/$', views.home, name="home"),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^login/$', auth_views.login, { 'template_name': 'bellybean/login.html' }, name='login'),
    url(r'^logout/$', auth_views.logout, { 'template_name': 'bellybean/logout.html', 'next_page': reverse_lazy('land') }, name='logout')
]