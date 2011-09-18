from django.test import TestCase
from django.test.client import Client
from lxml import html
from utils import *

class TestHomePage(TestCase):

  def setUp(self):
    self.client = Client()
    self.quote = create_test_quote()
    self.dom = '' 
    self.quotes = []

  def tearDown(self):
    self.quote = ''
    self.dom = ''
    self.quotes = []

  def __load_dom(self):
    response = self.client.get('/')
    self.dom = html.fromstring(response.content)

  def testHomePageResponse(self):
    response = self.client.get('/')
    self.failUnlessEqual(response.status_code, 200)

  def testHomePageShouldHaveTheRightTitle(self):
    self.__load_dom()
    assert self.dom.cssselect('h1 a')[0].text, 'def programming:'

  def testHomePageShouldListQuotes(self):
    self.__load_dom()
    assert len(self.dom.cssselect('div.box')), 1
    assert self.dom.cssselect('div.box cite')[0].text, 'Test quote'
    assert self.dom.cssselect('div.box p.author a')[0].text, 'Author 1 and Author 2'
    assert self.dom.cssselect('div.box li.tags')[0].text, 'tagged under Tag 1, Tag 2'
    assert self.dom.cssselect('div.box cite a')[0].attrib['href'], '/quote/test-quote/'

  def testHomePageShouldShowMenu(self):
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

  def testHomePageShouldShowPagination(self):
    self.quotes = create_multiple_test_quotes()
    self.__load_dom()
    assert len(self.dom.cssselect('div.pagination')), 1
