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
    #pass

    if type(features) is str:
        features = features.split(",")
        features = [feature.strip(" ") for feature in features]
        print(features)

    base_features = HAYES["a"]
    base_features = [phonetic.strip('-') for phonetic in base_features]
    base_features = [phonetic.strip('0') for phonetic in base_features]
    base_features = [phonetic.strip('+') for phonetic in base_features]
    zero_features = ["0"+phonetic for phonetic in base_features]
    negative_features = ["-"+phonetic for phonetic in base_features]
    positive_features = ["+"+phonetic for phonetic in base_features]
    total_features = zero_features + positive_features + negative_features
    print(total_features)

    for feature in features:
        if feature not in total_features:
            raise ValueError(feature+" does not exist as a feature")

    counter = 0;
    match_list = []
    for line in HAYES:
        match = set(features) & set(HAYES[line])
        #raise ValueError(''.join(features)+" does not exist as a feature")
        if len(match) == len(features):
            match_list.append(HAYES[line])
            counter = counter + 1
    if counter < num:
        print("there are only "+str(counter)+" "+''.join(features)+" segments")
    if num == -1:
        return match_list
    else:
        return match_list[0:num]
