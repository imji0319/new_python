# 캐시 문제
'''
캐시교체 알고리즘 LRU를 사용.
cache hit -> 실행시간 1
cache miss -> 실행시간 5
'''

from typing import List
import collections
def solution(cachesize : int , cities : List[str]) -> int  :
    elapsed : int = 0
    cache = collections.deque(maxlen = cachesize) # 길이가 제한된 자료형

    for c in cities :
        c = c.lower() #  대소문자구분 X

        # 캐시 히트
        if c in cache :
            cache.remove(c)
            cache.append(c)
            elapsed +=1

        # 캐시 미스
        else :
            cache.append(c)
            elapsed +=5

    return elapsed 





