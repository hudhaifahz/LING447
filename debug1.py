#This script should open the example file, and put the spelling and
#transcription in one dictionary, and the spelling and frequency in another.
#Then, look only for words that have a frequency of at least 10, and from among
#those, look only for words that end in a vowel.
#Print this final list of words to screen.

vowels = ['a','e','i','o','u']
file = open('/Users/hudhaifahz/Desktop/LING447/example.txt', encoding='utf-8')#add the appropriate path to the example.txt file
headers = file.readline()
lexicon = dict()
freq_count = dict()
for line in file:
    line = line.split(',')
    lexicon[line[1]] = line[2]
    freq_count[line[1]] = line[0]
file.close()

data = list()
for word in lexicon:
    if freq_count[word] > 10:
        break
    transcription = word[lexicon]
    if transcription[-1] not in vowels:
        continue
    else:
        data.append(transcription)
print(data)
