def solution(word):
    alph = 'AEIOU'
    li = []

    def dfs(path):
        if len(path) > 5: return
        li.append(path)

        for i in alph:
            s = path + i
            dfs(s)

    for i in alph:
        dfs(i)

    answer = li.index(word) + 1

    return answer