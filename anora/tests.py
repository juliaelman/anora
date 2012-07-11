from django.utils import unittest
from anora.templatetags.anora import anora

class AnoraTestCase(unittest.TestCase):

	def test_anora(self):
		awords = ['rabbit', 'mole', 'fox']
		anwords = ['owl', 'ox', 'octopus']

		for an_a, word_list in (('a', awords), ('an', anwords)):
			for word in word_list:
				self.assertEqual(' '.join((an_a, word)), anora(word))