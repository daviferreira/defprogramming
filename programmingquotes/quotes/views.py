from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from quotes.models import Author, Tag, Quote
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
  quotes = Quote.objects.all().order_by('-id')
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
  return HttpResponse("Authors page")

def author_detail(request, slug):
  a = get_object_or_404(Author, slug=slug)
  quotes_by_author = a.quote_set.all().order_by('-id')
  return render_to_response('author_detail.html', {'author': a, 'quotes_by_author': quotes_by_author})

def tags(request):
  return HttpResponse("Tags page")

def tag_detail(request, slug):
  return HttpResponse("You're looking at tag %s." % slug)
