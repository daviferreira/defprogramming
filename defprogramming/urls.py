# coding: utf-8
from random import choice

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap

from rest_framework import routers, serializers, viewsets, generics

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

# Serializers define the API representation.
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'slug')


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Quote
        fields = ('body', 'authors', 'slug')

# ViewSets define the view behavior.
class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class RandomQuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all().order_by('?')[:1]
    serializer_class = QuoteSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'quotes', QuoteViewSet)
router.register(r'random', RandomQuoteViewSet)


urlpatterns = patterns(
    '',
    url(r'^', include('quotes.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^feed/$', LatestEntriesFeed(), name='feed'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    url(r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += staticfiles_urlpatterns()
