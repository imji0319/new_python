'''
Created on 2020. 9. 1.

@author: jihye
'''


import sys 

def misspelling(word):

    result = ""
    
    dataset = word.split('\n')
    
    for i in dataset[1:]:
        subset = i.split()
        
        num = int(subset[0])
        old_word = subset[-1]

        new_word = old_word[:num-1]+old_word[num:]

        result = result + str(num) + ' ' + new_word + '\n'
        
    return result


inputitems ="4\n4 MISSPELL\n1 PROGRAMMING\n7 CONTEST\n3 BALLOON"

rl = lambda: sys.stdin.readline()
tc = int(rl())

for t in range(tc):
    data = map(str, rl().split())

    num = int(data[0])
    
    old_word = data[-1]
    
    new_word = old_word[:num-1]+old_word[num]
    
    
    print (str(num)+' '+new_word)

    