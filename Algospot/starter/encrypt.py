'''
Created on 2020. 9. 2.

@author: jihye
'''



case = int(input())

for i in range(case):
    
    word = input()
    
    new_word =""
    for j in range(0,len(word),2):
        new_word += word[j]
        
    for n in range(1,len(word),2):
        new_word += word[n]

    
    print(new_word)
    

