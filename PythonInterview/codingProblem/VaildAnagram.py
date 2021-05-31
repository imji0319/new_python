
def isAnagram(s : str, t: str) -> bool :
    return sorted(s) == sorted(t)

'''
애너그램은 문자열 안에 동일한 요소가 같은 개수로 있을 경우이다. 
'''