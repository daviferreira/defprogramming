# coding: utf-8
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from .models import Author, Tag, Quote
from .forms import QuoteForm


PER_PAGE = 25


def index(request, page):
    featured_quote = Quote.objects.filter(featured=True).order_by('?')[:1][0]
    quotes = Quote.objects.all() \
                          .exclude(id=featured_quote.id) \
                          .order_by('-publish_date')
    quotes = __validates_pagination(page, Paginator(quotes, PER_PAGE))
    title = "defprogramming: quotes about coding"
    description = "Quotes about programming, coding, computer science, " \
                  "debugging, software industry, startups and motivation."
    base_url_pagination = reverse('root')
    return render_to_response('quotes/index.html',
                              locals(),
                              context_instance=RequestContext(request))


def detail(request, slug):
    quote = get_object_or_404(Quote, slug=slug)
    return render_to_response('quotes/detail.html',
                              locals(),
                              context_instance=RequestContext(request))


def random(request):
    quote = Quote.objects.order_by('?')[0]
    return render_to_response('quotes/detail.html',
                              locals(),
                              context_instance=RequestContext(request))


def authors(request):
    authors = Author.objects.all().order_by('name')
    title = "Listing all authors | defprogramming"
    description = "List of all the authors with quotes published. Quotes " \
                  "about programming, coding, software industry."
    return render_to_response('quotes/authors.html',
                              locals(),
                              context_instance=RequestContext(request))


def author_detail(request, slug, page=1):
    author = get_object_or_404(Author, slug=slug)
    quotes = author.quote_set.all().order_by('-publish_date')
    quotes = __validates_pagination(page, Paginator(quotes, PER_PAGE))
    authors = Author.objects.all().order_by('name')
    title = "Programming quotes by " + author.name + " | defprogramming"
    description = "Listing all programming quotes by " + author.name + \
                  ". Quotes about programming, coding, software industry."
    base_url_pagination = reverse('author', kwargs={'slug': slug})
    return render_to_response('quotes/author_detail.html',
                              locals(),
                              context_instance=RequestContext(request))


def tags(request):
    tags = Tag.objects.all().order_by('name')
    title = "Listing all tags | defprogramming"
    description = "Tags list. Quotes about programming, coding, software " \
                  "industry."
    return render_to_response('quotes/tags.html',
                              locals(),
                              context_instance=RequestContext(request))


def tag_detail(request, slug, page=1):
    tag = get_object_or_404(Tag, slug=slug)
    quotes = tag.quote_set.all().order_by('-publish_date')
    quotes = __validates_pagination(page, Paginator(quotes, PER_PAGE))
    tags = Tag.objects.all().order_by('name')
    title = "Programming quotes tagged under " + tag.name + " | defprogramming"
    description = "Listing all programming quotes tagged under " + tag.name + \
                  ". Quotes about programming, coding, software industry."
    base_url_pagination = reverse('tag', kwargs={'slug': slug})
    return render_to_response('quotes/tag_detail.html',
                              locals(),
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


def __validates_pagination(page, paginator):
    page = page or 1
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)
