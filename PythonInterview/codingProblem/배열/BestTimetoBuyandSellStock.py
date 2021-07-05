'''
Created on 2020. 10. 1.

@author: jihye
'''

'''
한번의 거래로 낼 수 있는 최대의 이익을 산출하라
input : List[int]
output : int
'''


from typing import List
import sys


# 브루트 포스 -> 타임 아

def maxProfit(prices : List[int]) -> int :
    
    max_price = 0 
    
    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)
            
    return max_price
   
   
    
def maxProfit2(prices : List[int]) -> int:
    
    
    # sys.maxsize() 함수를 통해 시스템의 최대( - 최소) 값을 지정 해 둔다. 
    profit = 0
    min_price = sys.maxsize()
    
    
    # 최소값과 최대값을 계속 갱신 
    
    for price in prices:
        
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
        
    return profit
        
        




if __name__ == '__main__':
    pass