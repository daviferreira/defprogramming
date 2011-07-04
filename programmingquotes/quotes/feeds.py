from django.contrib.syndication.feeds import Feed

from quotes.models import Quote

class RecentQuotes(Feed):
  title = 'Define programming: Recent quotes'
  link = '/'

  def items(self):
    return Quote.objects.all()

  def item_link(self, quote):
    return quote.get_absolute_url()
