from django.test import TestCase

from .utils import word_count


class WordCountFormTestCase(TestCase):

    def test_word_count_util(self):
        text_block = 'there are four lights'
        kwargs = word_count(text_block)
        self.assertEqual(kwargs['text_block'], text_block)
        self.assertEqual(kwargs['word_count'], len(text_block.split()))
        self.assertEqual(kwargs['extra_tokens'], 0)
