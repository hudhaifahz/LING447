vowels = ['a','e','i','o','u']
consonants = ['g', 'h', 'm', 'n', 't', 's', '\'']
words = ['gag0', 'huti', 'tagu', 'sisi', 'ga\'a', 'maui', 'magu', 'manaha', 'a\'u', 'momoe']
paumari = ['va.in.i', 'ka.jo.a','ja.o.o.ro', 'go.a', 'ko.a', 'a.fo.ro.ni', 'bo.vi.ri', 'ka.jo.vi.ri', 'a.ha.ka.ba.ra', 'so.hi.ri.ba.na.ki']

komering = ['hongas','nyuah','mati','ju\'','pukul','buru','paca\'','tari\'','dongi','nyanyi','jual','poros','karu\'','muntah','cawako']

vowel_count = 0
cons_count = 0
dot = '.'

for word in words:
    for letter in word:
        if letter in vowels:
            vowel_count = vowel_count +1
        #else: cons_count = cons_count +1
        else:
            if letter in consonants:
                cons_count = cons_count +1
            else:
                print (letter, 'is not a letter')

print (vowel_count)
print (cons_count)

splitword = paumari[0].split('.')
print (splitword)
#paumari[0].upper()
#paumari[0].lower()

for x in paumari:
    syllables = x.split('.')
    #print syllables
    syl_count = len(syllables)
    #print len(syllables)
    if syl_count > 3:
        #print ('in the word', x, 'the stress should be on', syllables[-3])
        target = -3
    else:
        target = -1
        print ('in the word', x, 'the stress should be on', syllables[-1])
        syllables[-1] = syllables[-1].upper()
        syllables = '.'.join(syllables)
        print(syllables)


    #else:
        #print x, 'has less than 3 variables'
        #print ('in the word', x, 'the stress should be on', syllables[-1])
        #syllables[-1] = syllables[-1].upper()
        #syllables = '.'.join(syllables)
        #print(syllables)

prefix = ''
for word in komering:
    initial = word[0]
    if initial in ['p','b']:
        prefix = 'ngam'
    elif initial in ['k']+vowels:
        prefix = 'ng'
    elif initial in ['t','d']:
        prefix = 'ngan'
    elif initial in ['c','j','s']:
        prefix = 'ngany'
    else:
        prefix = 'nga'
    if initial in ['p','k','t']:
        print('prefix is',prefix,'for word',word,'resulting in', prefix + word[1:])
    else: print('prefix is',prefix,'for word',word,'resulting in', prefix + word)
