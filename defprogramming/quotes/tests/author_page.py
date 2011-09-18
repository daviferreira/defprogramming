from django.test import TestCase
from django.test.client import Client
from lxml import html
from utils import *

class testAuthorPage(TestCase):

  def setUp(self):
    self.client = Client()
    self.dom = '' 
    self.author = create_test_author()

  def tearDown(self):
    self.dom = ''
    self.author = ''

  def __load_dom(self):
    response = self.client.get('/author/author/')
    self.dom = html.fromstring(response.content)

  def testAuthorPageResponse(self):
    response = self.client.get('/author/author/')
    self.failUnlessEqual(response.status_code, 200)
    
  def testAuthorPageShouldHaveTheRightTitle(self):
    self.__load_dom()
    assert self.dom.cssselect('h1')[0].text, 'Quotes by Author'
    
  def testAuthorPageShouldListAuthorsQuotes(self):
    self.__load_dom()
    assert len(self.dom.cssselect('div.box')), 10
    
  def testAuthorPageShouldHaveLinkToGoBackToTheHomePage(self):
    self.__load_dom()
    home_link = self.dom.cssselect('p.back a')
    assert len(home_link), 1
    assert home_link[0].text, '&larr; go back to the home page'
    assert home_link[0].attrib['href'], '/'