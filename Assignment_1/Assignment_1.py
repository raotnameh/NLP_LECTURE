import glob, string, re
from nltk.tokenize import sent_tokenize, word_tokenize
import spacy
from word2number import w2n
import string


path = glob.glob("data/20_newsgroups/rec.motorcycles/*")
path = glob.glob("data/20_newsgroups/sci.med/*")

vowels = ['a', 'e', 'i', 'o', 'u']
consonants = set(' '.join(string.ascii_lowercase).split()) - set(vowels)
punctutaions= set(' '. join(string.punctuation).split())


def open_(path):
    with open(path, "rb") as f:
        try: return f.read().decode("utf8")
        except: f.read()

# txt_files = [open_(i) for i in path]
# txt_files = [open_('data/20_newsgroups/rec.motorcycles/103117')]
# txt_files = [open_('data/20_newsgroups/sci.med/58045')]
txt_files = [open_('data/20_newsgroups/rec.motorcycles/102616')]
print(f"Number of total file: {len(txt_files)}")


def para_to_sent(txt):
    '''
    converts an input txt file to sentences
    txt = input txt file in string format
    '''
    return sent_tokenize(re.sub(' +', ' ',txt))
def sent_to_tokens(txt):
    '''
    converts an input sentence to words
    txt = input txt file in string format
    '''
    return word_tokenize(txt)

def words_(tokens, punctutaions):
    return [i for i in tokens if i not in punctutaions]


def num_2_c(words):
    return [i for i in words if i[0] in consonants]

def num_2_v(words):
    return [i for i in words if i[0] in vowels]

def find_email(sents):
    '''
    sents: A list containing the txt
    returns a list of all the email id's present in the list given
            the email ids has a "." in it.
    '''
    dummy = []
    for i in sents:
        if re.findall(r"\b\S+@\S+\b",i):
            dummy.append(re.findall(r"\b\S+@\S+\.+\S+\b",i))
    return [i for j in dummy for i in j]

def task_4(sents,given_word):
    '''
    
    '''
    dummy = []
    for _i in sents:        
        if re.findall(fr"^{given_word} \b",_i.lower()):
            dummy.append(_i)
    return dummy

def task_5(sents,given_word):
    '''
    
    '''
    dummy = []
    for _i in sents:
        if re.findall(fr"\b {given_word}[.?!""'']*$",_i.lower()):
            dummy.append(_i)
    return dummy

def task_6(words,sents,given_word):
    '''
    
    '''
    sents_ = [i for i in sents if re.findall(fr"\b{given_word}\b",i.lower())]
    
    return sents_

def task_7(sents):
    '''
    
    '''
    return [i for i in sents if re.findall(r"\?$",i) is None]

def task_8(para):
    '''
    
    '''
    dummy = []
    for i in re.findall(r"[0-9]+[0-9]+:[0-9]+[0-9]+:[0-9]+[0-9]+", para):
        time = i.split(":")
        dummy.append(time[-2] + ' mins, ' +time[-1] + ' sec')
    return dummy

def task_9(para):
    '''
    
    '''
    return [i for j in para for i in re.findall(fr"[A-Z]+[a-z]*[0-9]*[A-Z]+[a-z]*[0-9]*",j)]

