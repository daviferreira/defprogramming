from django.test import TestCase
from django.test.client import Client
from lxml import html
from utils import *

class testTagPage(TestCase):

  def setUp(self):
    self.client = Client()
    self.dom = '' 
    self.tag = create_test_tag()

  def tearDown(self):
    self.dom = ''
    self.tag = ''

  def __load_dom(self):
    response = self.client.get('/tag/tag/')
    self.dom = html.fromstring(response.content)
  
  def testTagPageResponse(self):
    response = self.client.get('/tag/tag/')
    self.failUnlessEqual(response.status_code, 200)
    
  def testTagPageShouldHaveTheRightTitle(self):
    self.__load_dom()
    assert self.dom.cssselect('h1')[0].text, 'Quotes by Tag'
    
  def testTagPageShouldListTagsQuotes(self):
    self.__load_dom()
    assert len(self.dom.cssselect('div.box')), 10
    
  def testTagPageShouldHaveLinkToGoBackToTheHomePage(self):
    self.__load_dom()
    home_link = self.dom.cssselect('p.back a')
    assert len(home_link), 1
    assert home_link[0].text, '&larr; go back to the home page'
    assert home_link[0].attrib['href'], '/'