'''
Created on 2020. 9. 28.

@author: jihye
'''

'''
소주 만병만 주소 

'''

def LongestPalindrome(s : str) -> str :
    
    # 예외 처리 
    if len(s) < 2 or s[:] == s[::-1]:
        return s 
    
    # 팰린드롬 판별 및 투 포인트 확장 
    def expand(left : int, right: int) -> str:
        
        while left >= 0 and right <= len(s) and s[left] == s[right-1] : 
            left -= 1
            right += 1
            
        return s[left+1 : right -1]
    
    result = ''
    
    # 슬라이딩 윈도우 우측으로 이동 
    
    for i in range(len(s)-1):
        
        result = max(result, 
                     expand(i, i+1), 
                     expand(i, i+2),
                     key = len )
    return result 



def main():
    
    s = "babad"
    print(LongestPalindrome(s))
    
    s= "cbbd"
    print(LongestPalindrome(s))

if __name__ == '__main__':
    main()