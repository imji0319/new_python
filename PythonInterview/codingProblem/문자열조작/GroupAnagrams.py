'''
Created on 2020. 9. 28.

@author: jihye
'''

'''
문자열 배열을 받아 애너그램 단위로 그룹핑하라.
애너그램 Anagram : 일종의 언어유희로 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 말함.


input : 문자열 리스트 
output  : 리스트 배열 

'''

from typing import List
import collections



def GroupAnagrams(strs: List[str]) -> List[List[str]]:
    
    # KeyError : defaultdict 
    anagrams = collections.defaultdict(list)  # class : list 
    
    for word in strs:
        # add to anagrams list after sorting 
        # print(''.join(sorted(word)))
        anagrams[''.join(sorted(word))].append(word)
    
    return anagrams.values()


def main():
    strs = ["eat" ,"tea","tan","ate","nat","bat"]
    print(GroupAnagrams(strs))


if __name__ == '__main__':
    main()