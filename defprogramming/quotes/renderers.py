# coding: utf-8
from django_medusa.renderers import StaticSiteRenderer

from .models import Quote, Author, Tag


class QuotesRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = [
            '/',
            '/authors/',
            '/tags/',
            '/random/',
            '/submit/',
            '/sitemap.xml',
        ]

        for data in [Quote, Author, Tag]:
            items = data.objects.all()
            for item in items:
                paths.append(item.get_absolute_url())

        return paths

renderers = [QuotesRenderer, ]
