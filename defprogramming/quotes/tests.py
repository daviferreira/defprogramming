from datetime import datetime
from django.test import TestCase
from django.test.client import Client
from lxml import html
from quotes.models import Author, Tag, Quote

class TestQuote(TestCase):

  def setUp(self):
    self.quote = create_test_quote()

  def tearDown(self):
    self.quote = ''

  def testModels(self):
    self.assertEqual(self.quote.authors.all().count(), 2)
    self.assertEqual(self.quote.tags.all().count(), 2)

class TestIndexPage(TestCase):

  def setUp(self):
    self.client = Client()
    self.quote = create_test_quote()
    self.dom = '' 
    self.quotes = []

  def tearDown(self):
    self.quote = ''
    self.dom = ''
    self.quotes = []

  def testIndexPage(self):
    response = self.client.get('/')
    self.failUnlessEqual(response.status_code, 200)

  def testAuthorsPage(self):
    response = self.client.get('/authors/')
    self.failUnlessEqual(response.status_code, 200)  
    
  def testTagsPage(self):
    response = self.client.get('/tags/')
    self.failUnlessEqual(response.status_code, 200)

  def testIndexPageShouldHaveTheRightTitle(self):
    self.__load_dom()
    assert self.dom.cssselect('h1 a')[0].text, 'def programming:'

  def testIndexPageShouldListQuotes(self):
    self.__load_dom()
    assert len(self.dom.cssselect('div.box')), 1
    assert self.dom.cssselect('div.box cite')[0].text, 'Test quote'
    assert self.dom.cssselect('div.box p.author a')[0].text, 'Author 1 and Author 2'
    assert self.dom.cssselect('div.box li.tags')[0].text, 'tagged under Tag 1, Tag 2'

  def testIndexPageShouldShowMenu(self):
    self.__load_dom()
    menu_links = self.dom.cssselect('footer p span.menu a')
    assert len(menu_links), 6 
    assert menu_links[0].text, 'Home'
    assert menu_links[0].attrib['href'], '/'
    assert menu_links[1].text, 'Random Quote'
    assert menu_links[1].attrib['href'], '/random'
    assert menu_links[2].text, 'Authors'
    assert menu_links[2].attrib['href'], '/authors'
    assert menu_links[3].text, 'Tags'
    assert menu_links[3].attrib['href'], '/tags'
    assert menu_links[4].text, 'Feed'
    assert menu_links[4].attrib['href'], '/feed'
    assert menu_links[5].text, 'Submit Quote'
    assert menu_links[5].attrib['href'], '/submit'

  def testeIndexPageShouldShowPagination(self):
    self.quotes = create_multiple_test_quotes()
    self.__load_dom()
    assert len(self.dom.cssselect('div.pagination')), 1

  def __load_dom(self):
    response = self.client.get('/')
    self.dom = html.fromstring(response.content)

def create_test_quote():
  body = 'Test quote'
  now = datetime.now()
  quote = Quote.objects.create(body=body, publish_date=now)
  quote.authors.create(name='Author 1')
  quote.authors.create(name='Author 2')
  quote.tags.create(name='Tag 1')
  quote.tags.create(name='Tag 2')
  return quote

def create_multiple_test_quotes(ammount = 100):
  quotes = []
  for i in xrange(ammount):
    body = 'Test quote %d' % i
    now = datetime.now()
    quote = Quote.objects.create(body=body, publish_date=now)
    quote.authors.create(name='Author 1')
    quote.authors.create(name='Author 2')
    quote.tags.create(name='Tag 1')
    quote.tags.create(name='Tag 2')
    quotes.append(quote)
  return quotes
