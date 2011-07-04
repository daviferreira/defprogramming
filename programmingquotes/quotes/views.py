from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from quotes.models import Author, Tag, Quote
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
  quotes = Quote.objects.all().order_by('-publish_date')
  paginator = Paginator(quotes, 10)
  
  page = request.GET.get('page') or 1
  try:
    quotes = paginator.page(page)
  except PageNotAnInteger:
    quotes = paginator.page(1)
  except EmptyPage:
    quotes = paginator.page(paginator.num_pages)
  
  return render_to_response('index.html', {'quotes': quotes})
  
def detail(request, slug):
  q = get_object_or_404(Quote, slug=slug)
  return render_to_response('detail.html', {'quote': q})

def authors(request):
  authors = Author.objects.all().order_by('name')
  return render_to_response('authors.html', {'authors': authors})

def author_detail(request, slug):
  a = get_object_or_404(Author, slug=slug)
  quotes = a.quote_set.all().order_by('-publish_date')
  
  paginator = Paginator(quotes, 10)
  
  page = request.GET.get('page') or 1
  try:
    quotes = paginator.page(page)
  except PageNotAnInteger:
    quotes = paginator.page(1)
  except EmptyPage:
    quotes = paginator.page(paginator.num_pages)
  
  return render_to_response('author_detail.html', {'author': a, 'quotes': quotes})

def tags(request):
  tags = Tag.objects.all().order_by('name')
  return render_to_response('tags.html', {'tags': tags})

def tag_detail(request, slug):
  t = get_object_or_404(Tag, slug=slug)
  quotes = t.quote_set.all().order_by('-publish_date')
  
  paginator = Paginator(quotes, 10)
  
  page = request.GET.get('page') or 1
  try:
    quotes = paginator.page(page)
  except PageNotAnInteger:
    quotes = paginator.page(1)
  except EmptyPage:
    quotes = paginator.page(paginator.num_pages)
  
  return render_to_response('tag_detail.html', {'tag': t, 'quotes': quotes})
