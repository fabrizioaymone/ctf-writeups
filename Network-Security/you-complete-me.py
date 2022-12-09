import string

word=''
poss_words = [word]
counts= [3952, 825, 23, 3,2, 2, 1, 1, 1, 1, 1, 1, 1]

with open('words.txt', 'r') as file:
    words = file.read()

words = words.split('\n')


for j in range(13):
    next_poss_words=[]
    for poss_word in poss_words:
        for i in string.ascii_lowercase:
            count=0
            for w in words:
                if w.startswith(poss_word+i):
                    count+=1
            if count == counts[j]:
                next_poss_words.append(poss_word+i)
    poss_words = next_poss_words
    print(poss_words)
print(next_poss_words)
        
