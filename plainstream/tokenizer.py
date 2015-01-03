
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize


class Tokenizer(object):

    def __init__(self, language, normalize=False, train_text_gen=None):
        """
        A tokenizer using NLTK Penn Treebank tokenizer, and the Punkt sentence tokenizer.
        Params:
        language: Language to tokenize (currently doesn't do anything)
        train_text_gen: A generator of training text for the sentence tokenizer.
        """
        self.language = language
        self.train_text_gen = train_text_gen
        self.normalize = normalize
        
        if train_text_gen:
            self.sent_tokenizer = self._train_sentence_tokenizer()
        else:
            self.sent_tokenizer = PunktSentenceTokenizer()

    def _train_sentence_tokenizer(self):
        return PunktSentenceTokenizer(train_text="\n".join(self.train_text_gen))

    def tokenize(self, text):
        tokenized = []
        for sentence in self.sent_tokenizer.tokenize(text):
            tokenized_sentence = []
            for word in word_tokenize(sentence):
                if self.normalize:
                    word = word.lower()
                tokenized_sentence.append(word)
            tokenized.append(tokenized_sentence)

        return tokenized
