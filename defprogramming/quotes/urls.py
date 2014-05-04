# coding: utf-8
from django.conf import settings
from django.conf.urls import patterns
from django.conf.urls import url
from django.views.decorators.cache import cache_page

from .views import QuoteDetailView, AuthorDetailView, TagDetailView


urlpatterns = patterns(
    'quotes.views',
    url(
        regex=r'^q/(?P<uuid>[\w]+)/$',
        view=cache_page(settings.DEFAULT_CACHE_TIME)(
            QuoteDetailView.as_view()
        ),
        name='quote'
    ),
    # url(r'^q/(?P<uuid>[\w]+)/$', 'detail', name='quote'),
    url(r'^quote/(?P<slug>[\w-]+)/$', 'quote_redirect'),

    url(
        regex=r'^quotes-by/(?P<slug>[\w-]+)/(page/(?P<page>\d+)/)?$',
        view=cache_page(settings.DEFAULT_CACHE_TIME)(
            AuthorDetailView.as_view()
        ),
        name='author'
    ),
    url(r'^authors/$', 'authors', name='authors'),

    url(r'^tags/$', 'tags', name='tags'),
    url(
        regex=r'^quotes-tagged-with/(?P<slug>[\w-]+)/(page/(?P<page>\d+)/)?$',
        view=cache_page(settings.DEFAULT_CACHE_TIME)(
            TagDetailView.as_view()
        ),
        name='tag'
    ),

    url(r'^random/$', 'random', name='random'),
    url(r'^submit/$', 'submit_quote', name='submit'),

    url(
        r'^(page/(?P<page>\d+)/)?(format/(?P<format>\w+)/)?$',
        'index',
        name='root'
    ),
)
