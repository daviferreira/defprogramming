from django.test import TestCase
from utils import *

class TestQuote(TestCase):

  def setUp(self):
    self.quote = create_test_quote()

  def tearDown(self):
    self.quote = ''

  def testModels(self):
    self.assertEqual(self.quote.authors.all().count(), 2)
    self.assertEqual(self.quote.tags.all().count(), 2)