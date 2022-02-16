## 리벤슈타인 거리 (편집거리) 알고리즘
## 동적 프로그래밍 예제

def levenshtein(s1, s2, debug = False ):
    if len(s1) < len(s2):
        return levenshtein(s2, s1, debug) # 길이 긴 것 기준

    if len(s2) == 0:
        return len(s1)


    previous_row = range(len(s2) + 1)

    for i , c1 in enumerate(s1):
        current_row  =[ i + 1 ]

        for j, c2 in enumerate(s2):
            insertions = previous_row[j+1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != C2)

            current_row.append(min(insertions,
                                   deletions,
                                   substitutions))

        if debug :
            print(current_row[1:])
        previous_row = current_row


    return previous_row[-1]

s1 = '꿈을꾸는아이'
s2 = '아이오아이'

print(levenshtein(s1, s2, debug=True)

