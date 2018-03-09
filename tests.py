# -*- coding: utf-8 -*-
import unittest
from homoglyphs import Homoglyphs, STRATEGY_LOAD, STRATEGY_IGNORE, STRATEGY_REMOVE


class TestCommon(unittest.TestCase):
    def test_detect_category(self):
        self.assertEqual(Homoglyphs.detect_category('d'), 'LATIN')
        self.assertEqual(Homoglyphs.detect_category('Д'), 'CYRILLIC')
        self.assertEqual(Homoglyphs.detect_category('?'), 'COMMON')

    def test_get_alphabet(self):
        alphabet = Homoglyphs.get_alphabet(['LATIN'])
        self.assertIn('s', alphabet)
        self.assertIn('S', alphabet)
        self.assertNotIn('ё', alphabet)
        self.assertGreater(len(alphabet), 50)
        self.assertLess(len(alphabet), 1400)

        alphabet = Homoglyphs.get_alphabet(['CYRILLIC'])
        self.assertIn('ё', alphabet)
        self.assertIn('Ё', alphabet)
        self.assertNotIn('s', alphabet)
        self.assertGreater(len(alphabet), 50)
        self.assertLess(len(alphabet), 500)

    def test_get_table(self):
        alphabet = Homoglyphs.get_alphabet(['LATIN'])
        table = Homoglyphs.get_table(alphabet)
        self.assertIn('s', table)
        self.assertNotIn('к', table)

    def test_get_char_variants(self):
        variants = Homoglyphs(['LATIN'])._get_char_variants('s')
        self.assertIn('s', variants)
        self.assertIn('ｓ', variants)
        self.assertNotIn('S', variants)
        self.assertNotIn('ё', variants)

        variants = Homoglyphs(['LATIN'])._get_char_variants('c')
        self.assertIn('c', variants)
        self.assertNotIn('с', variants)  # CIRILLIC SMALL ES

        variants = Homoglyphs(['LATIN', 'CYRILLIC'])._get_char_variants('c')
        self.assertIn('c', variants)
        self.assertIn('с', variants)  # CIRILLIC SMALL ES

    def test_strategy(self):
        variants = Homoglyphs(['LATIN'], strategy=STRATEGY_IGNORE)._get_char_variants('ё')
        self.assertEqual(variants, ['ё'])

        variants = Homoglyphs(['LATIN'], strategy=STRATEGY_LOAD)._get_char_variants('х')  # CIRILLIC
        self.assertGreater(len(variants), 1)
        self.assertIn('x', variants)  # LATIN
        self.assertIn('х', variants)  # CIRILLIC

        variants = Homoglyphs(['LATIN'], strategy=STRATEGY_REMOVE)._get_char_variants('х')  # CIRILLIC
        self.assertEqual(variants, [])


if __name__ == '__main__':
    unittest.main()
