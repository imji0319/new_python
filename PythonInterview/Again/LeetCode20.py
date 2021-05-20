# 괄호로 된 입력값이 올바른지 판별

def valid(s :str):
    stack = []

    table = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    for i in s:
        if i not in table:
            stack.append(i)

        elif not stack or table[i] != stack.pop():
            return False

    return len(stack) == 0

