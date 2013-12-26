from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^browserid/', include('django_browserid.urls')),

    # Examples:
    # url(r'^$', 'hatch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^list/', include('simplelist.urls', namespace='simplelist')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('simplelist.urls', namespace='simplelist')),
)
