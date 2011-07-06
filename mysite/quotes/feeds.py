from django.contrib.syndication.views import Feed
from quotes.models import Author, Quote
import re

class LatestEntriesFeed(Feed):
    title = "def programming: latest quotes"
    link = "/"
    description = "Latest published quotes from defprogramming.com"

    def items(self):
        return Quote.objects.order_by('-publish_date')[:20]

    def item_title(self, item):
      authors = ""
      for author in item.authors.all():
        authors += author.name + " and "
      return re.sub(r' and $', '', authors)

    def item_description(self, item):
        return item.body
