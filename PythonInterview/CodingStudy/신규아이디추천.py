import re


def solution(new_id):
    answer = ''
    # print(new_id)
    # 1단계
    id = new_id.lower()
    # 2단계

    id = re.findall(r'([\w\.\_\-])', id)
    id = ''.join(id)

    # 3단계
    id = re.sub('[.]{1,}', '.', id)

    # 4단계
    if id[0] == '.':
        id = id[1:]

    if len(id) != 0:
        if id[-1] == '.':
            id = id[:-1]

    # 5단계
    if len(id) == 0:
        id = 'a'

    # 6단계
    if len(id) > 15:
        id = id[:15]

    if id[-1] == '.':
        id = id[:-1]

    # 7단계
    if len(id) <= 2:
        # id += id[-1]
        while True:
            id += id[-1]
            if len(id) == 3:
                break

    answer = id

    return answer