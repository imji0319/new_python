'''
Created on 2020. 9. 28.

@author: jihye
'''


'''
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 
대소문자 구분을 하지 않으며, 구두점 또한 무시한다. 

output : most common word
'''
from typing import List
import collections 
import re


'''
collections.Counter() : dict subclass for counting hashable objects

'''


def MostCommonWord(paragraph : str, banned: List[str]) -> str:
    
    words = [ word for word in re.sub(r'[\W]', ' ', paragraph) # 문자가 아닌 문자 제외 \W or ^\w 
             .lower() #소문자처리 
             .split() # return list 
             if word not in banned ]
    
    counts = collections.Counter(words) # counts dictionary 
    
    return counts.most_common(1)[0][0]  # [0] : (key, value) [0][0] : key
    
   
def main():
    
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
    banned = ["hit"]
    
    print (MostCommonWord(paragraph, banned))


if __name__ == '__main__':
    main()