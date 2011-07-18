from django.test import TestCase
from splinter.browser import Browser
from quotes.models import Author, Tag, Quote

class TestQuote(TestCase):
  browser = Browser()

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def testIndexPage(self):
    self.browser.visit("http://localhost:8000")
    assert self.browser.is_element_present_by_css('div.box cite')
