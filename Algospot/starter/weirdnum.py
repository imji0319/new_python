'''
Created on 2020. 8. 31.

@author: jihye
'''



def weirdnum(n):
    
    from itertools import permutations
    import numpy as np
    
    def subset_sum(sublist, n):
    
        j = list(set([tuple(set(i)) for i in permutations(sublist, n)]))
            
        yield j

    
    # divisors add to list 
    
    divide_list=[]

                       
    for i in range(1, n): 
        if i not in (divide_list) and n % i == 0 :
            divide_list.append(i)
            divide_list.append(n//i)
    
    divide_list.remove(n)
    
    # sum of divisors 
    listsum = 0
    for i in divide_list:
        listsum = listsum + i
    
    #subset_list=[]
    result = "weird"


    if n > (listsum-n):
        #print(divide_list, len(divide_list))

        for i in range(len(divide_list),1,-1):
            
            gener = subset_sum(divide_list, i)
            
            for j in gener:
                #print(j)
                #print(np.sum(j, axis=1))
                
                if (n  in np.sum(j, axis = 1)):
                    result = "not weird"
                    return result


    return result
    
    
print(weirdnum(12))
print(weirdnum(70))
print(weirdnum(836))
print(weirdnum(1575))