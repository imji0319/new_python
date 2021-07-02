

# 브루트 포스
def fibo_b(N: int ) -> int:
    if N<=1:
        return 1
    return fibo_b(N-1)+fibo_b(N-2)



# 메모이제이션
# 메모이제이션(memoization)은 컴퓨터 프로그램이 동일한 계산을 반복해야 할 때,
# 이전에 계산한 값을 메모리에 저장함으로써 동일한 계산의 반복 수행을 제거하여 프로그램 실행 속도를 빠르게 하는 기술이다.
import collections
class Solution :
    dp = collections.defaultdict()

    def fibo_m(self, N :int ) -> int:

        if N <= 1:
            return 1

        if self.dp[N]:
            return self.dp[N]

        self.dp[N] = self.fibo_m(N-1) + self.fibo_m(N-2)
        return self.dp[N]


# 타뷸레이션
class Solution2:
    dp = collections.defaultdict()

    def fib(self, N : int) -> int :
        self.dp[1] = 1

        for i in range(2, N+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]

        return self.dp[N]

# 두 변수만 이용
def fibo_2(N : int)->int:
    x, y = 0, 1

    for i in range(0, N):
        x, y = y, x+y

    return x

# 행렬
import numpy as np
def fib_M(n):
    M = np.matrix([[0,1],
                   [1,1]])

    vec = np.matrix([[0],
                     [1]])

    return np.matmul(M**n, vec)[0]









