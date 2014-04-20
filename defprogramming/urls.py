# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
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
    'quotes.views',
    url(r'^quote/(?P<slug>[\w_-]+)/$', 'detail', name='quote'),
    # url(r'^quote/(?P<quote_id>\d+)/$', 'detail'),
    # TODO: (r'^quote/(?P<quote_uuid>\d+)/$', 'detail'),
    url(r'^authors/$', 'authors', name='authors'),
    url(r'^quotes-by/(?P<slug>[\w_-]+)/(page/(?P<page>\d+)/)?$', 'author_detail', name='author'),
    # url(r'^author/(?P<slug>[\w_-]+)/$', 'author_detail'),
    # url(r'^author/(?P<author_id>\d+)/$', 'author_detail'),
    url(r'^tags/$', 'tags', name='tags'),
    url(r'^quotes-tagged-with/(?P<slug>[\w_-]+)/(page/(?P<page>\d+)/)?$', 'tag_detail', name='tag'),
    # url(r'^tag/(?P<slug>[\w_-]+)/$', 'tag_detail'),
    # url(r'^tag/(?P<tag_id>\d+)/$', 'tag_detail'),
    url(r'^random/$', 'random', name='random'),
    url(r'^submit/$', 'submit_quote', name='submit'),
    url(r'^(page/(?P<page>\d+)/)?$', 'index', name='root'),
)

urlpatterns += [
    url(r'^feed/$', LatestEntriesFeed(), name='feed'),
]

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    url(r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += staticfiles_urlpatterns()
