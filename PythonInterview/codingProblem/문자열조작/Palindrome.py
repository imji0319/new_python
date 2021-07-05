'''
Created on 2020. 9. 27.

@author: jihye
'''




'''
Palindrome = 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장 : 회문 

ex) 소주 만병만 주소 

input : string list 
output : bool


'''

# 풀이 1

def isPalindrome( s: str ) -> bool:
    
    strs = []

    for char in s :
        if char.isalnum(): # isalnum() : 영문자, 숫자 여부를 판별하는 함수 
            strs.append(char.lower())

    # 펠린드롬 여부 판별         
    while len(strs) > 1:
        '''
        pop(0) = 0의 위치를 지정
        pop(0) !=  pop() : 맨 앞과 끝 값을 호출하는 동시에 삭제 
        '''
        if strs.pop(0) != strs.pop() : 
            return False 
    
    return True

# 풀이 2

def isPalindrome2(s : str) -> bool:
    
    '''
    자료형 데크 Deque 로 선언 
    Deque : 더블 엔디드 큐 ( Double-Ended Queue )의 줄임말로, 
    글자그대로 야옥 끝을 모두 추출할 수 있는, 큐를 일반화한 형태의 추상 자료형 (ADT) 
    
    '''
    strs = collections.deque()
    
    for char in s : 
        if char.isalnum():
            strs.append(char.lower())
    
    # popleft() :O(1) 로 성능 개선 <-> pop(0) : O(n)
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
        
    return True
        
   
def isPalindrome3(s : str) -> bool:
    
    s = s.lower()
    
    # re filtering  -> 한번에 영숫자만 걸러냄 
    s = re.sub('[^a-z0-9]','',s)
    
    return s == s[::-1] # [::-1] 뒤집을 수 있음 



def main():
    s = 'A man, a plan, a canal : Panama'
    result = isPalindrome(s)
    print(s, ':', result)
    
    s = 'race a car'
    result = isPalindrome2(s)
    print(s, ':', result)
    
    
    s = 'A man, a plan, a canal : Panama'
    result = isPalindrome3(s)
    print(s, ':', result)



if __name__ == '__main__' :
    main()
    
    
    