from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from quotes.models import Author, Tag, Quote
from django.http import HttpResponse

def index(request):
  latest_quotes_list = Quote.objects.all().order_by('-id')[:20]
  return render_to_response('index.html', {'latest_quotes_list': latest_quotes_list})
  
def detail(request, slug):
  q = get_object_or_404(Quote, slug=slug)
  return render_to_response('detail.html', {'quote': q})

def authors(request):
  return HttpResponse("Authors page")

def author_detail(request, slug):
  return HttpResponse("You're looking at author %s." % slug)

def tags(request):
  return HttpResponse("Tags page")

def tag_detail(request, slug):
  return HttpResponse("You're looking at tag %s." % slug)
