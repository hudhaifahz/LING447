wordlist = ['lempar','rasa','wakil','jakin','masak','nikah','isi','ambil','word']
for word in wordlist:
    for n in range(len(word)):
        if word[n] == 'a':
            if n == len(word)-1:
                print (word[n-1]+'_#')
            elif n == 0:
                print ('#_'+word[n+1])
            else:
                print (word[n-1]+'_'+word[n+1])
