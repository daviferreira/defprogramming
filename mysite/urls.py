from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from quotes.models import Quote, Author, Tag
admin.autodiscover()

from quotes.feeds import LatestEntriesFeed

quotes = {
  'queryset': Quote.objects.all(),
  'date_field': 'publish_date'
}

authors = {
  'queryset': Author.objects.all()    
}

tags = {
  'queryset': Tag.objects.all()    
}

sitemaps = {
  'quotes': GenericSitemap(quotes, changefreq = 'weekly', priority=0.6),
  'authors': GenericSitemap(authors, changefreq = 'weekly', priority=0.6),
  'tags': GenericSitemap(tags, changefreq = 'weekly', priority=0.6),
}

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
    (r'^random/?$', 'random'),
    (r'^$', 'index'),
)

urlpatterns += patterns('quotes.feeds',
  (r'^feed/$', LatestEntriesFeed()),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

urlpatterns += staticfiles_urlpatterns()
