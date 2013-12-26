from django.conf.urls import patterns, url

from simplelist import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<list_id>\d+)/$', views.detail, name='detail'),

)
