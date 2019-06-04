from django.conf.urls import url
from . import views
import django.views.defaults

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.leden_list, name='leden_list'),
    url(r'^over_ons/$', views.over_ons, name='over_ons'),
    url(r'^fotos/$', views.fotos, name='fotos'),
    url(r'^activiteiten/$', views.activiteiten, name='activiteiten'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^leden/$', views.leden_list, name='leden'),
    url(r'^lunas/$', views.luna_list, name='lunas'),
    url(r'^zonnestraaltjes/$', views.zonnie_list, name='zonnestraaltjes'),
    url(r'^agenda/$', views.agenda, name='agenda'),

    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^404/$', django.views.defaults.page_not_found, ),
    url(r'^picture/new/$', views.picture_new, name='picture_new'),
]