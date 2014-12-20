plainstream
========

Sometimes you just need a lot of text. Plainstream is a Python application that provides you with a plain text stream directly from Wikipedia in any of its supporting languages.

Usage
-----

As a Python module:

    import plainstream
    for sentence in plainstream.get_text('en', max_words=20000, tokenize=True):
        print(line)

Example output:

    ['Anarchism', 'is', 'a', 'political', 'philosophy', 'that', 'advocates', 'stateless', 'societies', 'often', 'defined', 'as', 'self-governed', 'voluntary', 'institutions', ',', 'but', 'that', 'several', 'authors', 'have', 'defined', 'as', 'more', 'specific', 'institutions', 'based', 'on', 'non-hierarchical', 'free', 'associations', '.']
    ...


Command line:

    usage: plainstream [-h] -l LANGUAGE [-w WORDS] [-b BYTES] [--tokenize]
                       [--train_sentence_tokenizer]

    Stream text from Wikipedia.

    optional arguments:
      -h, --help            show this help message and exit
      -l LANGUAGE, --language LANGUAGE
                            Language code according to ISO_639-1, e.g. en, sv
      -w WORDS, --words WORDS
                            Maximum number of words to print (only works for
                            space-separated languages).
      -b BYTES, --bytes BYTES
                            Maximum number of bytes to print.
      --tokenize            Tokenize the text and output one word per line,
                            sentences split with newline.
      --train_sentence_tokenizer
                            For non-English text it might raise the quality to
                            train the sentence segmenter. This increases the
                            startup time.

Example output:

    plainstream -l en -w 20000 --tokenize

    Anarchism
    is
    a
    political
    philosophy    
    ...


Installation
------------
`python setup.py install`

Compatibility
-------------
Tested on python 3.4.

Acknowledgements
----------------

Thanks to the developers of WikiExtractor.py, [Medialab](http://medialab.di.unipi.it/wiki/Wikipedia_Extractor), for providing the Wikipedia plain text parser. 

