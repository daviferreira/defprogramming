from datetime import datetime
from django.test import TestCase
from django.test.client import Client
from lxml import html
from quotes.models import Author, Tag, Quote

class TestQuote(TestCase):

  def setUp(self):
    self.client = Client()
    body = "Test quote"
    now = datetime.now()
    self.quote = Quote.objects.create(body=body, publish_date=now)
    self.quote.authors.create(name="Author 1")
    self.quote.authors.create(name="Author 2")
    self.quote.tags.create(name="Tag 1")
    self.quote.tags.create(name="Tag 2")

  def tearDown(self):
    pass

  def test_models(self):
    self.assertEqual(self.quote.authors.all().count(), 2)
    self.assertEqual(self.quote.tags.all().count(), 2)

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
    response = self.client.get('/')
    dom = html.fromstring(response.content)
    assert dom.cssselect('h1 a')[0].text, "def programming:"

  def testIndexPageShouldListQuotes(self):
    pass

  def testIndexPageShouldShowMenu(self):
    pass

  def testeIndexPageShouldShowPagination(self):
    pass
