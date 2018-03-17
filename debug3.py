#This loads a small corpus of Cherokee words and extracts all the words
#that have something to do with trees. This done simply by checking the
#English gloss in the text file, and if it has the word "tree" in it,
#we should keep that word
#At the end, print out all the tree words

path = 'c:\\users\\scott\\documents\\linguistics\\ling447\\cherokee.txt'
cherokee = dict()
file = open(path, mode='r', encoding='utf-8'):
for line in file:
    line = line.split(',')
    syllables = line[1]
    roman = line[2]
    gloss = line[3]
    cherokee[roman] = gloss
file.close()

cherokee = load_file(path)
tree_words = list()
for word in cherokee:
    if 'tree' in cherokee[word]:
        tree_words.append(word)
    else:
        break
print(tree words)
