# Homoglyphs

![Homoglyphs logo](logo.png)
[![Build Status](https://travis-ci.org/orsinium/homoglyphs.svg?branch=master)](https://travis-ci.org/orsinium/homoglyphs) [![PyPI version](https://img.shields.io/pypi/v/homoglyphs.svg)](https://pypi.python.org/pypi/homoglyphs) [![Status](https://img.shields.io/pypi/status/homoglyphs.svg)](https://pypi.python.org/pypi/homoglyphs) [![Code size](https://img.shields.io/github/languages/code-size/orsinium/homoglyphs.svg)](https://github.com/orsinium/homoglyphs) [![License](https://img.shields.io/pypi/l/homoglyphs.svg)](LICENSE)

Homoglyphs -- python library for getting [homoglyphs](https://en.wikipedia.org/wiki/Homoglyph) and converting to ASCII.


## Features

It's smarter version of [confusable_homoglyphs](https://github.com/vhf/confusable_homoglyphs):

* Autodect or manual choosing category ([aliases from ISO 15924](https://en.wikipedia.org/wiki/ISO_15924#List_of_codes)).
* Auto or manual load only needed alphabets in memory.
* Converting to ASCII.
* More configurable.
* More stable.


## Installation

```bash
sudo pip install homoglyphs
```


## Usage

Best way to explain something is show how it works. So, let's have a look on the real usage.

Importing:

```python
import homoglyphs as hg
```

### Languages

```python
#detect
hg.Languages.detect('w')
# {'pl', 'da', 'nl', 'fi', 'cz', 'sr', 'pt', 'it', 'en', 'es', 'sk', 'de', 'fr', 'ro'}
hg.Languages.detect('т')
# {'mk', 'ru', 'be', 'bg', 'sr'}
hg.Languages.detect('.')
# set()

# get alphabet for languages
hg.Languages.get_alphabet(['ru'])
# {'в', 'Ё', 'К', 'Т', ..., 'Р', 'З', 'Э'}

# get all languages
hg.Languages.get_all()
# {'nl', 'lt', ..., 'de', 'mk'}
```

### Categories

Categories -- ([aliases from ISO 15924](https://en.wikipedia.org/wiki/ISO_15924#List_of_codes)).

```python
#detect
hg.Categories.detect('w')
# 'LATIN'
hg.Categories.detect('т')
# 'CYRILLIC'
hg.Categories.detect('.')
# 'COMMON'

# get alphabet for categories
hg.Categories.get_alphabet(['CYRILLIC'])
# {'ӗ', 'Ԍ', 'Ґ', 'Я', ..., 'Э', 'ԕ', 'ӻ'}

# get all categories
hg.Categories.get_all()
# {'RUNIC', 'DESERET', ..., 'SOGDIAN', 'TAI_LE'}
```

### Homoglyphs

Get homoglyphs:

```python
# get homoglyphs (latin alphabet initialized by default)
hg.Homoglyphs().get_combinations('q')
# ['q', '𝐪', '𝑞', '𝒒', '𝓆', '𝓺', '𝔮', '𝕢', '𝖖', '𝗊', '𝗾', '𝘲', '𝙦', '𝚚']
```

Alphabet loading:

```python
# load alphabet on init by categories
homoglyphs = hg.Homoglyphs(categories=('LATIN', 'COMMON', 'CYRILLIC'))  # alphabet loaded here
homoglyphs.get_combinations('гы')
# ['rы', 'гы', 'ꭇы', 'ꭈы', '𝐫ы', '𝑟ы', '𝒓ы', '𝓇ы', '𝓻ы', '𝔯ы', '𝕣ы', '𝖗ы', '𝗋ы', '𝗿ы', '𝘳ы', '𝙧ы', '𝚛ы']

# load alphabet on init by languages
homoglyphs = hg.Homoglyphs(languages={'ru', 'en'})  # alphabet will be loaded here
homoglyphs.get_combinations('гы')
# ['rы', 'гы']

# manual set alphabet on init      # eng rus
homoglyphs = hg.Homoglyphs(alphabet='abc абс')
homoglyphs.get_combinations('с')
# ['c', 'с']

# load alphabet on demand
homoglyphs = hg.Homoglyphs(languages={'en'}, strategy=hg.STRATEGY_LOAD)
# ^ alphabet will be loaded here for "en" language
homoglyphs.get_combinations('гы')
# ^ alphabet will be loaded here for "ru" language
# ['rы', 'гы']
```

You can combine `categories`, `languages`, `alphabet` and any strategies as you want. The strategies specify how to handle any characters not already loaded:

* `STRATEGY_LOAD`: load category for this character
* `STRATEGY_IGNORE`: add character to result
* `STRATEGY_REMOVE`: remove character from result


### Converting glyphs to ASCII chars

```python
homoglyphs = hg.Homoglyphs(languages={'en'}, strategy=hg.STRATEGY_LOAD)

# convert
homoglyphs.to_ascii('тест')
# ['tect']
homoglyphs.to_ascii('ХР123.')  # this is cyrillic "х" and "р"
# ['XP123.', 'XPI23.', 'XPl23.']

# string with chars which can't be converted by default will be ignored
homoglyphs.to_ascii('лол')
# []

# you can set strategy for removing not converted non-ASCII chars from result
homoglyphs = hg.Homoglyphs(
    languages={'en'},
    strategy=hg.STRATEGY_LOAD,
    ascii_strategy=hg.STRATEGY_REMOVE,
)
homoglyphs.to_ascii('лол')
# ['o']

# also you can set up range of allowed char codes for ascii (0-128 by default):
homoglyphs = hg.Homoglyphs(
    languages={'en'},
    strategy=hg.STRATEGY_LOAD,
    ascii_strategy=hg.STRATEGY_REMOVE,
    ascii_range=range(ord('a'), ord('z')),
)
homoglyphs.to_ascii('ХР123.')
# ['l']
homoglyphs.to_ascii('хр123.')
# ['xpl']
```
