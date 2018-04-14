path = '/Users/hudhaifahz/Desktop/LING447/saisiyat.txt'
file = open(path, encoding='utf-8')
words = []
for line in file:
    line = line.strip()
    line = line.strip('\ufeff')
    line = line.split(',')
    #print(line)
    words.append(line[0])
file.close()
print (words)

redups = []
cawords = []
for word in words:
    if len(word)>0:
        #print(word[0])
        Ca = word[0]+'a'
        word = '-'.join([Ca,word])
        #word = Ca + word
        cawords.append(word)
print(cawords)
