# coding: utf-8
from django_medusa.renderers import StaticSiteRenderer

from .models import Quote, Author, Tag


class QuotesRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = set([
            '/',
            '/authors/',
            '/tags/',
            '/random/',
            '/submit/',
            '/sitemap.xml',
        ])

        for data in [Quote, Author, Tag]:
            items = data.objects.all()
            for item in items:
                paths.add(item.get_absolute_url())

        return list(paths)

renderers = [QuotesRenderer, ]
