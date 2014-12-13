plainstream
========

.. image:: https://pypip.in/v/plainstream/badge.png
    :target: https://pypi.python.org/pypi/plainstream
    :alt: Latest PyPI version

.. image:: False.png
   :target: False
   :alt: Latest Travis CI build status

Sometimes you just need a lot of text. Plainstream provides you with a plain text stream directly from Wikipedia in any of its supporting languages.

Usage
-----

As a Python module:

    import plaintext
    for line in plaintext.get_text('en'):
        print(line)


Command line:

    usage: plainstream [-h] -l LANGUAGE [-w WORDS] [-b BYTES]

    Stream text from Wikipedia.

    optional arguments:
      -h, --help            show this help message and exit
      -l LANGUAGE, --language LANGUAGE
                            Language to stream.
      -w WORDS, --words WORDS
                            Maximum number of words to print (approximate, only
                            works for space-separated languages).
      -b BYTES, --bytes BYTES
                            Maximum number of bytes to print (approximate).

Installation
------------
`python setup.py install`

Requirements
^^^^^^^^^^^^
requests

Compatibility
-------------
Tested on python 3.4

Licence
-------

Authors
-------

`plainstream` was written by `Jimmy Callin <jimmy.callin@gmail.com>`_.

