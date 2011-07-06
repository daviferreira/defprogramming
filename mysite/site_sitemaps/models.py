from django.contrib.sitemaps import Sitemap
from quotes.models import Quote

class QuotesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Quote.objects.order_by('-publish_date')

    def lastmod(self, obj):
        return obj.publish_date
