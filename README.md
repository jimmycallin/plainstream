plainstream
========

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
------------
requests

Compatibility
-------------
Tested on python 3.4

Licence
-------

MIT License.
