from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'DjangoRRD.rrd.views.list'),
    url(r'^info/(?P<rrd>(.*))/$', 'DjangoRRD.rrd.views.info'),
    url(r'^raw/(?P<rrd>(.*))/$', 'DjangoRRD.rrd.views.raw'),
    url(r'^data/(?P<rrd>(.*))/(?P<ds>(.*))/(?P<rra>(.*))/$', 'DjangoRRD.rrd.views.data'),
    url(r'^fresh/(?P<rrd>(.*))/(?P<ds>(.*))/(?P<rra>(.*))/$', 'DjangoRRD.rrd.views.fresh'),
    url(r'^graph/(?P<rrd>(.*))/$', 'DjangoRRD.rrd.views.graph'),
    # Examples:
    # url(r'^$', 'DjangoRRD.views.home', name='home'),
    # url(r'^DjangoRRD/', include('DjangoRRD.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
