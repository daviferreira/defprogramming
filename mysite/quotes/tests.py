from django.test import TestCase
from django.test.client import Client
from quotes.models import Author, Tag, Quote

class TestQuote(TestCase):

  def setUp(self):
    self.client = Client()
    pass

  def tearDown(self):
    pass

  def testIndexPage(self):
    response = self.client.get('/')
    self.failUnlessEqual(response.status_code, 200)

  def testAuthorsPage(self):
    response = self.client.get('/authors/')
    self.failUnlessEqual(response.status_code, 200)  
    
  def testTagsPage(self):
    response = self.client.get('/tags/')
    self.failUnlessEqual(response.status_code, 200)
