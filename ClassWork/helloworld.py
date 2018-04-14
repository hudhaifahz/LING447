print('Hello World!')
print(1+1)
print(1.0+2.0)
print('1+1')
print('1'+'1')
#print('1'+1)
print('lol')
print('ga\'a\nga\'a')
vowels = ['a','e','i','o','u']
for v in vowels:
    print (v)
words = ['gago', 'huti', 'tagu', 'sisi', 'ga\'a', 'maui', 'magu', 'manaha', 'a\'u', 'momoe']
total = 0.0
for w in words:
    length = len(w)
    total += length
print total
avg = total/len(words)
print len(words)
print avg
longest = ''
for w in words:
    length = len(w)
    if length > len(longest):
        longest = w
print longest
print len(words[4])
