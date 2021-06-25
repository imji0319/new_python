## https://www.acmicpc.net/problem/10872


nums = int(input())


def p(num):

    if num == 0 :
        return 1

    def dfs(n):
        if n == 1:
            return n

        result = n*dfs(n-1)

        return result

    return dfs(nums)

print(p(nums))
