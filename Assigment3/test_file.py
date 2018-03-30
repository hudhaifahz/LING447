import filefunctions

HAYES = filefunctions.load_hayes()

def find_longest_word(wordlist, num=1):
    #pass
    top_longest = {}
    for n in range(num):
        length = len(wordlist)
        longest = ""
        if length < 1:
            return "Word list is empty"
        else:
            for i in range(length):
                if len(wordlist[i]) > len(longest):
                    longest = wordlist[i]
                    #top_longest[wordlist[i]]=len(wordlist[i])
                else:
                    raise TypeError("wordlist contains non-string values")
                    #return "list contains an element that is not a string at index "+str(i)
        top_longest[longest] = len(longest)
        wordlist.remove(longest)
    return top_longest

#def compare(seg1, seg2, how="same"):
def compare(*args):
    #pass
    i = 0
    for arg in args:
        i = i+1
    if i == 2:
        seg1 = args[0]
        seg2 = args[1]
        how = "same"
    elif i == 3:
        how = args[0]
        seg1 = args[1]
        seg2 = args[2]
    try:
        seg1_list = HAYES[seg1]
        seg2_list = HAYES[seg2]
    except KeyError:
        raise ValueError(seg1+" or "+seg2+" do not appear in the Hayes dictionary")

    if how == "same":
        same = set(seg1_list) & set(seg2_list)
        same = [phonetic.strip('-') for phonetic in same]
        same = [phonetic.strip('0') for phonetic in same]
        same = [phonetic.strip('+') for phonetic in same]
        return same
    elif how == "diff":
        diff = set(seg1_list) - set(seg2_list)
        diff = [phonetic.strip('-') for phonetic in diff]
        diff = [phonetic.strip('0') for phonetic in diff]
        diff = [phonetic.strip('+') for phonetic in diff]
        return diff

def find_phonemes(features, num):
    pass


#TESTS

#print(HAYES['p'])
#print(HAYES['a'])

for feature in HAYES['z']:
    print(feature)
for feature in HAYES['q']:
    print(feature)

wordlist1 = ["hi","where","you"]
longestTest1 = find_longest_word(wordlist1,2)
print(longestTest1)

wordlist2 = ["hi","where",0]
longestTest2 = find_longest_word(wordlist2)
print(longestTest2)

compareTest1 = compare("how","p","a")
print(compareTest1)

compareTest2 = compare("same","oh","oh")
print(compareTest2)

sameTest1 = compare("same","p","a")
print(sameTest1)
twoargTest = compare("s","z")
print(twoargTest)
diffTest1 = compare("diff","s","z")
print(diffTest1)
diffTest2 = compare("same","p","o")
print(diffTest2)

segments1 = find_phonemes(['0anterior', '+approximant', '-back'], 5)
print(segments1)
segments2 = find_phonemes(['+nasal', '+voice'], 7)
print(segments2)
segments3 = find_phonemes(['+nasal', '+voice'], -1)
print(segments3)
segments4 = find_phonemes(['+high', '+low'], 5)
print(segments4)
segments5 = find_phonemes(['+sticky'], 5)
print(segments5)
segments6 = find_phonemes('+high, +low', 5)
print(segments6)
#for line in HAYES:
#    print(HAYES[line])
