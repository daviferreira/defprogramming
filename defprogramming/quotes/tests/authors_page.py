from django.test import TestCase
from django.test.client import Client
from lxml import html
from utils import *

class testAuthorsPage(TestCase):

  def setUp(self):
    self.client = Client()
    self.dom = '' 
    self.authors = []

  def tearDown(self):
    self.dom = ''
    self.authors = []

  def __load_dom(self):
    response = self.client.get('/authors/')
    self.dom = html.fromstring(response.content)

  def testAuthorsPageResponse(self):
    response = self.client.get('/authors/')
    self.failUnlessEqual(response.status_code, 200)  

  def testAuthorsPageShouldShowAuthors(self):
    self.authors = create_multiple_test_authors()
    self.__load_dom()
    authors_list = self.dom.cssselect('#authors-list li')
    assert len(authors_list), 100

  def testAuthorsPageShouldHaveLinkToGoBackToTheHomePage(self):
    self.__load_dom()
    home_link = self.dom.cssselect('p.back a')
    assert len(home_link), 1
    assert home_link[0].text, '&larr; go back to the home page'
    assert home_link[0].attrib['href'], '/'

  def testAuthorNameShouldHaveQuotesCount(self):
    self.authors = create_multiple_test_authors()
    self.__load_dom()
    assert self.dom.cssselect('#authors-list li a')[0].text, 'Author 0 (10)'