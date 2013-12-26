from django.conf.urls import patterns, url

from simplelist import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<list_id>\d+)/$', views.list_detail, name='list_detail'),
    url(r'^entry/(?P<pk>\d+)/$', views.EntryDetailView.as_view(), name='entry_detail'),
)
