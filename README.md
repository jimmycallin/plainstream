plainstream
========

Sometimes you just need a lot of text. Plainstream is a Python application that provides you with a plain text stream directly from Wikipedia in any of its supporting languages.

Usage
-----

As a Python module:

    import plainstream
    for line in plainstream.get_text('en'):
        print(line)


Command line:

    usage: plainstream [-h] -l LANGUAGE [-w WORDS] [-b BYTES]

    Stream text from Wikipedia.

    optional arguments:
      -h, --help            show this help message and exit
      -l LANGUAGE, --language LANGUAGE
                            Language code according to ISO_639-1, e.g. en, sv ...
      -w WORDS, --words WORDS
                            Maximum number of words to print (only works for
                            space-separated languages).
      -b BYTES, --bytes BYTES
                            Maximum number of bytes to print.

Installation
------------
`python setup.py install`

Compatibility
-------------
Tested on python 3.4.

Acknowledgements
----------------

Thanks to the developers of WikiExtractor.py, [Medialab](http://medialab.di.unipi.it/wiki/Wikipedia_Extractor), for providing the Wikipedia plain text parser. 

