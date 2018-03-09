# -*- coding: utf-8 -*-
from collections import defaultdict
import json
from itertools import product
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class Homoglyphs(object):
    def __init__(self, categories):
        alphabet = self.get_alphabet(categories)
        self.table = self.get_table(alphabet)

    def get_ranges(self, categories):
        with open(os.path.join(CURRENT_DIR, 'categories.json')) as f:
            data = json.load(f)
        indexes = []
        for category in categories:
            try:
                indexes.append(data['iso_15924_aliases'].index(category))
            except ValueError:
                raise ValueError('Invalid category: {}'.format(category))
        for point in data['code_points_ranges']:
            if point[2] in indexes:
                yield point[:2]

    def get_alphabet(self, categories):
        chars = []
        ranges = list(self.get_ranges(categories))
        for start, end in ranges:
            chars.extend(chr(code) for code in range(start, end))
        return ''.join(chars)

    def get_table(self, alphabet):
        table = defaultdict(list)
        with open(os.path.join(CURRENT_DIR, 'confusables.json')) as f:
            data = json.load(f)
        for char in alphabet:
            if char in data:
                for homoglyph in data[char]:
                    if homoglyph['c'] in alphabet:
                        table[char].append(homoglyph['c'])
        return table

    def _get_combinations(self, text):
        variations = []
        for char in text:
            # find alternative chars for current char
            alt_chars = self.table.get(char, [])
            # find alternative chars for alternative chars for current char
            alt_chars2 = [self.table.get(alt_char, []) for alt_char in alt_chars]
            # combine all alternatives
            alt_chars.extend(sum(alt_chars2, []))
            # add current char to alternatives
            alt_chars.append(char)

            # uniq, sort and add to variations
            alt_chars = sorted(list(set(alt_chars)))
            variations.append(alt_chars)

        for variant in product(*variations):
            yield ''.join(variant)

    def get_combinations(self, text):
        return list(self._get_combinations(text))

    def _to_ascii(self, text):
        for variant in self._get_combinations(text):
            if max(map(ord, variant)) < 256:
                yield variant

    def to_ascii(self, text):
        return list(self._to_ascii(text))
