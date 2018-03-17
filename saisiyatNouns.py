path = '/Users/hudhaifahz/Desktop/LING447/saisiyatNouns.txt'
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

redups = []
cawords = []
for word in words:
    if len(word)>0:
        #append first 3 to word then add var
        #print(word[0])
        Ca = word[0:3]
        #word = '-'.join([Ca,word])
        word = Ca + word + 'an'
        cawords.append(word)
print(cawords)

for n in range(len('lempar')):
    print( n, 'lempar'[n])
