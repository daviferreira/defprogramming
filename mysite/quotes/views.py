from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from quotes.models import Author, Tag, Quote
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
  quotes = Quote.objects.all().order_by('-publish_date')
  quotes = validates_pagination(request, Paginator(quotes, 10))
  return render_to_response('quotes/index.html', {'quotes': quotes})
  
def detail(request, slug):
  q = get_object_or_404(Quote, slug=slug)
  return render_to_response('quotes/detail.html', {'quote': q})

def random(request):
  q = Quote.objects.order_by('?')[0]
  return render_to_response('quotes/detail.html', {'quote': q})

def authors(request):
  authors = Author.objects.all().order_by('name')
  return render_to_response('quotes/authors.html', {'authors': authors})

def author_detail(request, slug):
  a = get_object_or_404(Author, slug=slug)
  quotes = a.quote_set.all().order_by('-publish_date')
  quotes = validates_pagination(request, Paginator(quotes, 10))  
  return render_to_response('quotes/author_detail.html', {'author': a, 'quotes': quotes})

def tags(request):
  tags = Tag.objects.all().order_by('name')
  return render_to_response('quotes/tags.html', {'tags': tags})

def tag_detail(request, slug):
  t = get_object_or_404(Tag, slug=slug)
  quotes = t.quote_set.all().order_by('-publish_date')
  quotes = validates_pagination(request, Paginator(quotes, 10))  
  return render_to_response('quotes/tag_detail.html', {'tag': t, 'quotes': quotes})
  
def validates_pagination(request, paginator):
  page = request.GET.get('page') or 1
  try:
    return paginator.page(page)
  except PageNotAnInteger:
    return paginator.page(1)
  except EmptyPage:
    return paginator.page(paginator.num_pages)
