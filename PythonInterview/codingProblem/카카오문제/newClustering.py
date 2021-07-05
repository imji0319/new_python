
# 자카드 유사도 : 두 집합 A,B 사이의 자카드 유사도 J(A,B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의
# 다중집합으로도 계산 가능


import re
import collections

def solution(str1 : str, str2: str) -> int :

    # 두 글자씩 끊어서 다중집합 구성

    str1s = [
        str1[i:i+2].lower()
        for i in range(len(str1) - 1)
        if re.findall('[a-z]{2}',str1[i:i+2].lower())
    ]

    str2s = [
        str2[i:i+2].lower()
        for i in range(len(str2) - 1)
        if re.findall('[a-z]{2}', str2[i:i+2].lower())
    ]

    # 교집합 계산
    intersection = sum((collections.Counter(str1s) &
                        collections.Counter(str2s)).values())

    # 합집합 계산
    union = sum((collections.Counter(str1s) |
                 collections.Counter(str2s)).values())


    # 자카드 유사도 계산
    jaccard_sim = 1 if union == 0 else intersection / union
    return int(jaccard_sim * 65536)




