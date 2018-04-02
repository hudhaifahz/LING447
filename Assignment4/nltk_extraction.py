import nltk
from nltk.book import *
from nltk.corpus import brown
import random
monty = text6[0:]
CLOSING_PUNCTUATION = ["!","?","."]
NUMBERS = ["0","1","2","3","4","5","6","7","8","9"]

#TASK 1

#first 10 sentences
first_ten = {}
i = 1
first_ten[i] = []
for x in monty:
    if x not in CLOSING_PUNCTUATION:
        first_ten[i].append(x+" ")
    else:
        first_ten[i].append(x)
        if i >= 10:
            break
        else:
            i = i+1
            first_ten[i] = []
#filtering words only and counting
counter = 0
for word in monty:
    if ((word == "I") or (len(word) > 1) or (word == "a") and word not in NUMBERS):
        counter = counter + 1
print('')
print('')
print('')
print('TASK #1')
print('')
print("Monty Python First Ten Sentences")
for sent in first_ten:
    print("sent"+str(sent)+": "+''.join(first_ten[sent]))
print('')
print("Monty Python Text Length (no filtering): " + str(len(monty)))
print("Monty Python Text Length (words only): " + str(counter))
print('')
#Monty Python Concordance of Coconut
print("Monty Python Concordance of Coconut: ")
text6.concordance("coconut")
print('')
#Monty Python Similarity of Knight
print("Monty Python Similarity of Knight: ")
text6.similar("knight")
print('')
print('')
print('')

#TASK 2

print('TASK #2')
print('')
#Full Text of UNDHR in Ibibio_Efik
print('Full Text of UNDHR in Ibibio_Efik:')
UDHR_ibibo_words = nltk.corpus.udhr.words('Ibibio_Efik-Latin1')[0:]
UDHR_ibibo = {}
j = 1
UDHR_ibibo[j] = []
for x in UDHR_ibibo_words:
    if x not in CLOSING_PUNCTUATION:
        UDHR_ibibo[j].append(x+" ")
    else:
        UDHR_ibibo[j].append(x)
        j = j+1
        UDHR_ibibo[j] = []
for sent in UDHR_ibibo:
    print(''.join(UDHR_ibibo[sent]))
print('')
#Length of UNDHR in Amahuaca
UNDHR_Amahuaca = nltk.corpus.udhr.words('Amahuaca-Latin1')[0:]
Amahuaca_counter = 0
for word in UNDHR_Amahuaca:
    if (len(word) > 1 and word not in NUMBERS):
        Amahuaca_counter = Amahuaca_counter + 1
print('Length of UNDHR in Amahuaca (words only): '+str(Amahuaca_counter))
#Length of UNDHR in Greenlandic
UNDHR_Greenlandic = nltk.corpus.udhr.words('Greenlandic_Inuktikut-Latin1')[0:]
Greenlandic_counter = 0
for word in UNDHR_Greenlandic:
    if (len(word) > 1 and word not in NUMBERS):
        Greenlandic_counter = Greenlandic_counter + 1
print('Length of UNDHR in Greenlandic (words only): '+str(Greenlandic_counter))
# Amahuaca is longer
if Greenlandic_counter > Amahuaca_counter:
    print("Greenlandic Has More Words")
else:
    print("Amahuaca Has More Words")
print('')
# first 5 words in turkish
UNDHR_Turkish = nltk.corpus.udhr.words('Turkish_Turkce-Turkish')[0:5]
print('First 5 Words of UNHDR in Turkish')
print (UNDHR_Turkish)
UNDHR_Turkish = [word+" " for word in UNDHR_Turkish]
print(''.join(UNDHR_Turkish))
print('')
print('')
print('')

#TASK 3

print('TASK #3')
print('')
#total categories
categories = brown.categories()
print('Brown Corpus Categories:')
print(categories)
print('')
#humor sentences
humor_sentences = brown.sents(categories='humor')
humor_sentences_length = len(humor_sentences)
random = random.randint(0,humor_sentences_length)
random_humor_sentence = humor_sentences[random]
print('Random Humor Sentence: ')
print(random_humor_sentence)
random_humor_sentence = [word+" " for word in random_humor_sentence]
print(''.join(random_humor_sentence))
print('')
#longest category
longest = ""
for category in categories:
    if len(brown.words(categories=category)) > len(longest):
        longest = category
print("The Category with the Most Words: "+longest)
