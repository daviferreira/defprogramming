from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from quotes.models import Author, Tag, Quote
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
  quotes = Quote.objects.all().order_by('-publish_date')
  quotes = validates_pagination(request, Paginator(quotes, 10))
  title = "def programming: quotes about coding"
  description = "Quotes about programming, coding, computer science, debugging, software industry, startups and motivation." 
  return render_to_response('quotes/index.html', locals(), context_instance=RequestContext(request))
  
def detail(request, slug):
  q = get_object_or_404(Quote, slug=slug)
  return render_to_response('quotes/detail.html', locals(), context_instance=RequestContext(request))

def random(request):
  q = Quote.objects.order_by('?')[0]
  return render_to_response('quotes/detail.html', locals(), context_instance=RequestContext(request))

def authors(request):
  authors = Author.objects.all().order_by('name')
  title = "Listing all authors | def programming"
  description = "List of all the authors with quotes published. Quotes about programming, coding, software industry.";
  return render_to_response('quotes/authors.html', locals(), context_instance=RequestContext(request))

def author_detail(request, slug):
  a = get_object_or_404(Author, slug=slug)
  quotes = a.quote_set.all().order_by('-publish_date')
  quotes = validates_pagination(request, Paginator(quotes, 10))  
  title = "Programming quotes by " + a.name + " | def programming"
  description = "Listing all programming quotes by " + a.name + ". Quotes about programming, coding, software industry." 
  return render_to_response('quotes/author_detail.html', locals(), context_instance=RequestContext(request))

def tags(request):
  tags = Tag.objects.all().order_by('name')
  title = "Listing all tags | def programming"
  description = "Tags list. Quotes about programming, coding, software industry.";
  return render_to_response('quotes/tags.html', locals(), context_instance=RequestContext(request))

def tag_detail(request, slug):
  t = get_object_or_404(Tag, slug=slug)
  quotes = t.quote_set.all().order_by('-publish_date')
  quotes = validates_pagination(request, Paginator(quotes, 10))  
  title = "Programming quotes tagged under " + t.name + " | def programming"
  description = "Listing all programming quotes tagged under " + t.name + ". Quotes about programming, coding, software industry." 

  return render_to_response('quotes/tag_detail.html', locals(), context_instance=RequestContext(request))
  
def validates_pagination(request, paginator):
  page = request.GET.get('page') or 1
  try:
    return paginator.page(page)
  except PageNotAnInteger:
    return paginator.page(1)
  except EmptyPage:
    return paginator.page(paginator.num_pages)
