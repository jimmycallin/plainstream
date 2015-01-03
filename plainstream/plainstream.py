import requests
import bz2
from . import parser
import sys

try:
    from .tokenizer import Tokenizer
except ImportError:
    pass

available_languages = {'aa','ab','af','ak','als','am','an','ang','ar','arc','as','ast','av','ay','az','ba','bar','bcl','be','bg','bh','bi','bm','bn','bo','bpy','br','bs','bug','bxr','ca','cbk_zam','cdo','ce','ceb','ch','cho','chr','chy','co','cr','crh','cs','csb','cu','cv','cy','da','de','diq','dsb','dv','dz','ee','el','eml','en','eo','es','et','eu','ext','fa','ff','fi','fiu_vro','fj','fo','fr','frp','fur','fy','ga','gan','gd','gl','glk','gn','got','gu','gv','ha','hak','haw','he','hi','hif','ho','hr','hsb','ht','hu','hy','hz','ia','id','ie','ig','ii','ik','ilo','io','is','it','iu','ja','jbo','jv','ka','kaa','kab','kg','ki','kj','kk','kl','km','kn','ko','kr','ks','ksh','ku','kv','kw','ky','la','lad','lb','lbe','lg','li','lij','lmo','ln','lo','lt','lv','mdf','mg','mh','mi','mk','ml','mn','mo','mr','mt','mus','my','myv','mzn','na','nah','nap','nds','nds_nl','ne','new','ng','nl','nn','no','nov','nrm','nv','ny','oc','om','or','os','pa','pag','pam','pap','pdc','pi','pih','pl','pms','ps','pt','qu','quality','rm','rmy','rn','ro','roa_rup','roa_tara','ru','rw','sa','sah','sc','scn','sco','sd','se','sg','sh','si','simple','sk','sl','sm','sn','so','sr','srn','ss','st','stq','su','sv','sw','szl','ta','te','tet','tg','th','ti','tk','tl','tlh','tn','to','tpi','tr','ts','tt','tum','tw','ty','udm','ug','uk','ur','uz','ve','vec','vi','vls','vo','wa','war','wo','wuu','xal','xh','yi','yo','za','zea','zh','zh_classical','zh_min_nan','zh_yue','zu'}

available_outputs = {'plaintext'}

tokenizer = {}

def get_text(language, 
             max_bytes=None, 
             max_words=None, 
             tokenize=False, 
             normalize=False,
             train_sentence_tokenizer=False, 
             output='raw'):
    """
    Returns a generator iteratively downloading text from Wikipedia dumps. 
    Parameters:
        language: Language code according to ISO_639-1, e.g. en, fr, sv, zh...
        max_bytes: Maximum number of bytes to download.
        max_words: Maximum number of words to download. Currently only works for languages with space-separated words.
        tokenize: Tokenize the text into word units. Currently uses the Penn Trebank tokenizer and Punkt sentence segmenter, 
                  and requires you to have NLTK installed. Outputted as one word per line, with two line breaks 
        normalize: Convert text to lower case. 
    """
    if language not in available_languages:
        raise RuntimeError("Language not supported.")

    if tokenize:
        train_text = None
        if train_sentence_tokenizer:
            train_text = get_text(language, max_words=10000, tokenize=False, train_sentence_tokenizer=False, output='plaintext')
        if language not in tokenizer:
            tokenizer[language] = Tokenizer(language, normalize=normalize, train_text_gen=train_text)

    dump_url = "http://dumps.wikimedia.org/{}wiki/latest/{}wiki-latest-pages-articles.xml.bz2".format(language, language)
    req = requests.get(dump_url, stream=True)
    with bz2.open(req.raw) as text:
        nbytes = 0
        nwords = 0
        for line in parser.parse(text):


            
            if tokenize:
                sentences = tokenizer[language].tokenize(line)
                for sentence in sentences:
                    if (max_bytes and nbytes >= max_bytes) \
                        or (max_words and nwords >= max_words):
                        return
                    nbytes += sys.getsizeof(sentence)
                    nwords += len(sentence)

                    yield sentence
            else:
                if (max_bytes and nbytes > max_bytes) \
                    or (max_words and nwords > max_words):
                    return
                nbytes += sys.getsizeof(line)
                nwords += len(line.split(" "))
                if normalize:
                    yield line.lower()
                else:
                    yield line
