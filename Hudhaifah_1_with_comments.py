import os
path = os.path.join(os.getcwd(),'vitu_nouns.txt')
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
    #just as a matter of style, you shouldn't have any spaces between function names and the brackets
    if word[-1] in vowels:
        suffixes[1] = word[-1]
        #it seems odd to modify the original list. I assume you're doing this because you
        #want to make it easiser to loop over, coming up next
        #I can't see a problem with this approach, I just wouldn't have considered doing it this way
        for suffix in suffixes:
            form = forms[i]
            i = i + 1
            #this counter variable isn't entirely necessary
            #since the variables "suffixes" and "forms" are the same length (they have to be)
            #you can just loop over the length of one of them, and re-use the same index, e.g
            #for n in range(len(forms)):
            #   form = forms[n]
            #   suffix = suffixes[n]
            vowel_final = word + "-" + suffix
            print (form + vowel_final)
    else:
        suffixes[1] = word[-2]
        lastVowel = word[-2]
        #this only words because the language is strictly CV syllables. If there were complex
        #codas, this might grab a consonant by accident
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

#Grade: A
#Really nice. I have a few pretty minor comments up above, but this is very well done.
