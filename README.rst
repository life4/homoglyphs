Homoglyphs
==========

|Homoglyphs logo| |Build Status| |PyPI version| |Status| |Code size|
|License|

Homoglyphs -- python library for getting
`homoglyphs <https://en.wikipedia.org/wiki/Homoglyph>`__ and converting
to ASCII.

Features
--------

It's smarter version of
`confusable\_homoglyphs <https://github.com/vhf/confusable_homoglyphs>`__:

-  Autodect or manual choosing category (`aliases from ISO
   15924 <https://en.wikipedia.org/wiki/ISO_15924#List_of_codes>`__).
-  Auto or manual load only needed alphabets in memory.
-  Converting to ASCII.
-  More configurable.
-  More stable.

Installation
------------

::

    sudo pip install homoglyphs

Usage
-----

Importing:

.. code:: python

    import homoglyphs as hg

Languages
~~~~~~~~~

.. code:: python

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

Categories
~~~~~~~~~~

Categories -- (`aliases from ISO
15924 <https://en.wikipedia.org/wiki/ISO_15924#List_of_codes>`__).

.. code:: python

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

Homoglyphs
~~~~~~~~~~

Get homoglyphs:

.. code:: python

    # get homoglyphs (latin alphabet initialized by default)
    hg.Homoglyphs().get_combinations('q')
    # ['q', '𝐪', '𝑞', '𝒒', '𝓆', '𝓺', '𝔮', '𝕢', '𝖖', '𝗊', '𝗾', '𝘲', '𝙦', '𝚚']

Alphabet loading:

.. code:: python

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

You can combine ``categories``, ``languages``, ``alphabet`` and any
strategies as you want.

Converting glyphs to ASCII chars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

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

.. |Homoglyphs logo| image:: logo.png
.. |Build Status| image:: https://travis-ci.org/orsinium/homoglyphs.svg?branch=master
   :target: https://travis-ci.org/orsinium/homoglyphs
.. |PyPI version| image:: https://img.shields.io/pypi/v/homoglyphs.svg
   :target: https://pypi.python.org/pypi/homoglyphs
.. |Status| image:: https://img.shields.io/pypi/status/homoglyphs.svg
   :target: https://pypi.python.org/pypi/homoglyphs
.. |Code size| image:: https://img.shields.io/github/languages/code-size/orsinium/homoglyphs.svg
   :target: https://github.com/orsinium/homoglyphs
.. |License| image:: https://img.shields.io/pypi/l/homoglyphs.svg
   :target: LICENSE
