Homoglyphs
==========

Homoglyphs -- python library for getting
`homoglyphs <https://en.wikipedia.org/wiki/Homoglyph>`__ and converting
to ASCII.

Features
--------

It's like
`confusable\_homoglyphs <https://github.com/vhf/confusable_homoglyphs>`__
but with some features:

-  Load only needed alphabet to memory.
-  Work as quick as possible.
-  Converting to ASCII.
-  More configurable.
-  More stable.

Usage
-----

.. code:: python

    from homoglyphs import Homoglyphs, STRATEGY_LOAD, STRATEGY_IGNORE, STRATEGY_REMOVE

    # detect category
    Homoglyphs.detect_category('s')
    # 'LATIN'
    Homoglyphs.detect_category('ё')
    # 'CYRILLIC'
    Homoglyphs.detect_category('.')
    # 'COMMON'

    # get latin combinations (by default initiated only latin alphabet)
    Homoglyphs().get_combinations('q')
    # ['q', '𝐪', '𝑞', '𝒒', '𝓆', '𝓺', '𝔮', '𝕢', '𝖖', '𝗊', '𝗾', '𝘲', '𝙦', '𝚚']

    # load alphabet on init by categories
    Homoglyphs(categories=('LATIN', 'COMMON', 'CYRILLIC')).get_combinations('гы')
    # ['rы', 'гы', 'ꭇы', 'ꭈы', '𝐫ы', '𝑟ы', '𝒓ы', '𝓇ы', '𝓻ы', '𝔯ы', '𝕣ы', '𝖗ы', '𝗋ы', '𝗿ы', '𝘳ы', '𝙧ы', '𝚛ы']

    # load alphabet by demand
    Homoglyphs(strategy=STRATEGY_LOAD).get_combinations('гы')
    # ['rы', 'гы', 'ꭇы', 'ꭈы', '𝐫ы', '𝑟ы', '𝒓ы', '𝓇ы', '𝓻ы', '𝔯ы', '𝕣ы', '𝖗ы', '𝗋ы', '𝗿ы', '𝘳ы', '𝙧ы', '𝚛ы']

    # convert to ASCII
    Homoglyphs(strategy=STRATEGY_LOAD).to_ascii('тест')
    # ['tect']
    Homoglyphs(strategy=STRATEGY_LOAD).to_ascii('ХР123.')  # this is cyrillic "х" and "р"
    # ['XP123.', 'XPI23.', 'XPl23.']

    # string with chars which can't be converted by default will be ignored
    Homoglyphs(strategy=STRATEGY_LOAD).to_ascii('лол')
    # []

    # you can set strategy for removing not converted non-ASCII chars from result
    Homoglyphs(strategy=STRATEGY_LOAD, ascii_strategy=STRATEGY_REMOVE).to_ascii('лол')
    # ['o']
