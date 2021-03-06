# coding: utf-8
import json

from django.conf import settings
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView

from .models import Author, Tag, Quote
from .forms import QuoteForm


PER_PAGE = 25


@cache_page(settings.DEFAULT_CACHE_TIME)
def index(request, page=1, format=None):
    try:
        featured_quote = Quote.objects.filter(featured=True) \
                                      .order_by('?')[:1][0]
        quotes = Quote.objects.all() \
                              .exclude(id=featured_quote.id)
    except IndexError:
        quotes = Quote.objects.all()
    quotes = Paginator(quotes, PER_PAGE).page(
        page or 1
    )

    if format == 'json':
        data = {
            'hasNext': quotes.has_next(),
            'quotes': []
        }
        for quote in quotes:
            data['quotes'].append(quote.serialize())
        return HttpResponse(json.dumps(data), mimetype='application/json')
    else:
        title = "defprogramming: quotes about coding"
        description = "Quotes about programming, coding, computer science, " \
                      "debugging, software industry, startups and motivation."
        base_url_pagination = reverse('root')
        return render_to_response('quotes/index.html',
                                  locals(),
                                  context_instance=RequestContext(request))


def quote_redirect(request, slug):
    quote = get_object_or_404(Quote, slug=slug)
    return HttpResponsePermanentRedirect(quote.get_absolute_url())


def random(request):
    quote = Quote.objects.order_by('?')[0]
    return render_to_response('quotes/random.html',
                              {'quote': quote},
                              context_instance=RequestContext(request))


def submit_quote(request):
    title = "Submit a quote | defprogramming"
    description = "Use this form to submit a quote. Please send only quotes " \
                  "about programming, coding, software industry."
    sent = False

    if request.method == 'POST':
        form = QuoteForm(request.POST)

        if form.is_valid():
            form.save(request.POST)
            sent = True

    else:
        form = QuoteForm()

    return render_to_response('quotes/submit_quote.html',
                              locals(),
                              context_instance=RequestContext(request))


class QuoteDetailView(DetailView):
    model = Quote

    def get_object(self):
        return get_object_or_404(Quote, uuid=self.kwargs['uuid'])


class DetailViewMixin(DetailView):

    def get_context_data(self, **kwargs):
        context = super(DetailViewMixin, self).get_context_data(**kwargs)

        quotes = self.object.quote_set.all()
        context['quotes'] = Paginator(quotes, PER_PAGE).page(
            self.kwargs.get('page') or 1
        )

        key = self.model._meta.verbose_name_plural.lower()
        context[key] = self.model.objects.extra(select={
            'name_lower': 'lower(name)'}
        ).order_by('name_lower')

        context['title'] = self.title % self.object.name
        context['description'] = self.description % self.object.name

        context['base_url_pagination'] = reverse(
            self.model.__name__.lower(),
            kwargs={
                'slug': self.object.slug
            }
        )

        return context


class AuthorListView(ListView):
    model = Author

    def get_queryset(self):
        return self.model.objects.extra(select={
            'name_lower': 'lower(name)'}
        ).order_by('name_lower')

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['title'] = "Listing all authors | defprogramming"
        context['description'] = "List of all the authors with quotes " \
                                 "published. Quotes about programming, " \
                                 "coding, software industry."
        return context


class AuthorDetailView(DetailViewMixin):
    model = Author
    title = "Programming quotes by %s | defprogramming"
    description = "Listing all programming quotes by %s. Quotes about " \
                  "programming, coding, software industry."


class TagListView(ListView):
    model = Tag

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context['title'] = "Listing all tags | defprogramming"
        context['description'] = "List of all the tags with quotes " \
                                 "published. Quotes about programming, " \
                                 "coding, software industry."
        return context


class TagDetailView(DetailViewMixin):
    model = Tag
    title = "Programming quotes tagged under %s | defprogramming"
    description = "Listing all programming quotes tagged under %s. "\
                  "Quotes about programming, coding, software industry."