def vowel_lowering(word):
    if '+voice' in final_features and '-voc' in final_features:
        if word[-2] == 'o':
            lowered = word[:-2]+'u'+word[-1]
        else:
            lowered = word
    else:
        lowered = word

def final_devoicing(word):
    if '+voice' in final_features and '-sonorant' in final_features:

        for sound in features:
            if '+voice' in features[sound]:
                continue
            for feature in features[sound][1:]:#skip over [voice]
                if feature not in features[final]:
                    break
            else:
                print(word, word[:-1]+sound)
    else:
        print(word, word)

def read_file(path):
    file = open(path, encoding = 'utf-8')
    file.readline()
    #this method reads exactly one line into a file. we don't want the first line anyway, because it's just
    #the titles of the columns, not actual polish data
    #As long as a file is open, Python will remember what line it was at, and the next time you read from
    #a file, the reading starts where it left off.
    #In this case, it means that when we start looping over the file in a just a few lines from here,
    #we're actually starting on the *second* line of the file, because we've already read the first one
    words = list()
    for line in file:
        line = line.strip()
        line = line.strip('\ufeff')
        if not line:
            continue #skip over blank lines
        line = line.split(',')
        words.append(line[0])
    file.close()
    return words

features = {'i': ['+voice', '+voc', '0cor', '+cont', '+high', '-low', '-back', '-lat', '-nasal', '+sonorant'],
            'p': ['-voice', '-voc', '-cor', '-cont', '-high', '-low', '-back', '-lat', '-nasal', '-sonorant'],
            'b': ['+voice', '-voc', '-cor', '-cont', '-high', '-low', '-back', '-lat', '-nasal', '-sonorant'],
            't': ['-voice', '-voc', '+cor', '-cont', '-high', '-low', '-back', '-lat', '-nasal', '-sonorant'],
            's': ['-voice', '-voc', '+cor', '+cont', '-high', '-low', '-back', '-lat', '-nasal', '-sonorant'],
            'e': ['+voice', '+voc', '0cor', '+cont', '-high', '-low', '-back', '-lat', '-nasal', '+sonorant'],
            'k': ['-voice', '-voc', '-cor', '-cont', '-high', '-low', '+back', '-lat', '-nasal', '-sonorant'],
            'a': ['+voice', '+voc', '-cor', '+cont', '-high', '+low', '-back', '-lat', '-nasal', '+sonorant'],
            'd': ['+voice', '-voc', '+cor', '-cont', '-high', '-low', '-back', '-lat', '-nasal', '-sonorant'],
            'l': ['+voice', '-voc', '+cor', '-cont', '-high', '-low', '-back', '+lat', '-nasal', '+sonorant'],
            'o': ['+voice', '+voc', '-cor', '+cont', '-high', '-low', '+back', '-lat', '-nasal', '+sonorant'],
            'h': ['-voice', '-voc', '-cor', '+cont', '-high', '-low', '+back', '-lat', '-nasal', '-sonorant'],
            'm': ['+voice', '-voc', '-cor', '-cont', '-high', '-low', '-back', '-lat', '+nasal', '+sonorant'],
            'n': ['+voice', '-voc', '+cor', '-cont', '-high', '-low', '-back', '-lat', '+nasal', '+sonorant'],
            'g': ['+voice', '-voc', '-cor', '-cont', '-high', '-low', '+back', '-lat', '-nasal', '-sonorant'],
            'u': ['+voice', '+voc', '-cor', '+cont', '+high', '-low', '+back', '-lat', '-nasal', '+sonorant'],
            'z': ['+voice', '-voc', '+cor', '+cont', '-high', '-low', '-back', '-lat', '-nasal', '-sonorant'],
            }

words = read_file('/Users/hudhaifahz/Desktop/LING447/newpolishlist.txt')
for word in words:
    final = word[-1]
    final_features = features[final]
    vowel_lowering(word)
    final_devoicing(word)
