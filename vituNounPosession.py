path = './vitu_nouns.txt'
file = open(path, encoding='utf-8')
words = []
for line in file:
    line = line.strip()
    line = line.strip('\n')
    line = line.strip('\ufeff')
    line = line.split(',')
    #print(line)
    if line[0]:
        words.append(line[0])
file.close()
print (words)

v = ""
suffixes = ["gu", v, "na", "miro", "doro", "moro", "hiro", "hita", "dolu", "miu", "dia"]
forms = ["singular 1st: ", "singular 2nd: ", "singular 3rd: ", "dual 1st inclusive: ", "dual 1st exclusive: ", "dual 2nd: ", "dual 3rd: ","plural 1st inclusive: ", "plural 1st exclusive: ", "plural 2nd: ", "plural 3rd: "]
vowels = ["a", "e", "i", "o", "u"]

for word in words:
    i = 0
    print (" ")
    print (word)
    if word[-1] in vowels:
        suffixes[1] = word[-1]
        for suffix in suffixes:
            form = forms[i]
            i = i + 1
            vowel_final = word + "-" + suffix
            print (form + vowel_final)
    else:
        suffixes[1] = word[-2]
        lastVowel = word[-2]
        for suffix in suffixes:
            form = forms[i]
            i = i + 1
            if suffix == "na":
                suffix = "a"
                consonant_final = word + "-" + suffix
            elif suffix in vowels:
                consonant_final = word + "-" + suffix
            else:
                consonant_final = word + "-" + lastVowel + suffix
            print (form + consonant_final)
