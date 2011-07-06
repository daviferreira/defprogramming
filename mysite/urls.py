from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

from quotes.feeds import LatestEntriesFeed
from site_sitemaps.models import QuotesSitemap

urlpatterns = patterns('quotes.views',
    (r'^quotes/$', 'index'),
    (r'^quote/(?P<slug>[\w_-]+)/$', 'detail'),
    (r'^quote/(?P<quote_id>\d+)/$', 'detail'),
    (r'^authors/$', 'authors'),
    (r'^author/(?P<slug>[\w_-]+)/$', 'author_detail'),
    (r'^author/(?P<author_id>\d+)/$', 'author_detail'),
    (r'^tags/$', 'tags'),
    (r'^tag/(?P<slug>[\w_-]+)/$', 'tag_detail'),
    (r'^tag/(?P<tag_id>\d+)/$', 'tag_detail'),
    #(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': QuotesSitemap}),
    (r'^$', 'index'),
)

urlpatterns += patterns('quotes.feeds',
  (r'^feed/$', LatestEntriesFeed()),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
