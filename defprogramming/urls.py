# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from quotes.models import Quote, Author, Tag
from quotes.feeds import LatestEntriesFeed


admin.autodiscover()


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
    'quotes': GenericSitemap(quotes, changefreq='weekly', priority=0.6),
    'authors': GenericSitemap(authors, changefreq='weekly', priority=0.6),
    'tags': GenericSitemap(tags, changefreq='weekly', priority=0.6),
}

urlpatterns = patterns(
    '',
    url(r'^', include('quotes.urls')),
    url(r'^feed/$', LatestEntriesFeed(), name='feed'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    url(r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += staticfiles_urlpatterns()
