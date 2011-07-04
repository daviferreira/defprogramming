from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from quotes.models import Author, Quote
from django.http import HttpResponse

def index(request):
  latest_quotes_list = Quote.objects.all().order_by('-id')[:20]
  return render_to_response('index.html', {'latest_quotes_list': latest_quotes_list})
  
def detail(request, quote_id):
  q = get_object_or_404(Quote, pk=quote_id)
  return render_to_response('detail.html', {'quote': q})

def authors(request):
  return HttpResponse("Authors page")

def author_detail(request, author_id):
  return HttpResponse("You're looking at author %s." % author_id)
