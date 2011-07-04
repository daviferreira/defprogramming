from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('quotes.views',
    (r'^quotes/$', 'index'),
    (r'^quote/(?P<quote_id>\d+)/$', 'detail'),
    (r'^authors/$', 'authors'),
    (r'^author/(?P<author_id>\d+)/$', 'author_detail'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
