"""
Stolen and little bit refactored:
https://github.com/vhf/confusable_homoglyphs/blob/master/confusable_homoglyphs/cli.py
"""


import re
from collections import defaultdict
from urllib.request import urlopen
import json
from pathlib import Path


path = Path('homoglyphs')


def generate_categories():
    """Generates the categories JSON data file from the unicode specification.
    """
    # inspired by https://gist.github.com/anonymous/2204527
    code_points_ranges = []
    iso_15924_aliases = []
    categories = []

    match = re.compile(r'([0-9A-F]+)(?:\.\.([0-9A-F]+))?\W+(\w+)\s*#\s*(\w+)',
                       re.UNICODE)

    url = 'ftp://ftp.unicode.org/Public/UNIDATA/Scripts.txt'
    file = urlopen(url).read().decode('utf-8').split('\n')
    for line in file:
        p = re.findall(match, line)
        if p:
            code_point_range_from, code_point_range_to, alias, category = p[0]
            alias = alias.upper()
            if alias not in iso_15924_aliases:
                iso_15924_aliases.append(alias)
            if category not in categories:
                categories.append(category)
            code_points_ranges.append((
                int(code_point_range_from, 16),
                int(code_point_range_to or code_point_range_from, 16),
                iso_15924_aliases.index(alias), categories.index(category))
            )
    code_points_ranges.sort()

    categories_data = {
        'iso_15924_aliases': iso_15924_aliases,
        'categories': categories,
        'code_points_ranges': code_points_ranges,
    }

    with (path / 'categories.json').open('w') as stream:
        stream.write(json.dumps(categories_data, indent=2, sort_keys=True))


def generate_confusables():
    """Generates the confusables JSON data file from the unicode specification.
    """
    url = 'ftp://ftp.unicode.org/Public/security/latest/confusables.txt'
    file = urlopen(url).read().decode('utf-8').split('\n')
    confusables_matrix = defaultdict(list)
    match = re.compile(r'[0-9A-F ]+\s+;\s*[0-9A-F ]+\s+;\s*\w+\s*#'
                       r'\*?\s*\( (.+) → (.+) \) (.+) → (.+)\t#',
                       re.UNICODE)
    for line in file:
        p = re.findall(match, line)
        if p:
            char1, char2, name1, name2 = p[0]
            confusables_matrix[char1].append(char2)
            confusables_matrix[char2].append(char1)

    with (path / 'confusables.json').open('w') as stream:
        stream.write(json.dumps(confusables_matrix, indent=2, sort_keys=True))


if __name__ == '__main__':
    generate_categories()
    generate_confusables()
