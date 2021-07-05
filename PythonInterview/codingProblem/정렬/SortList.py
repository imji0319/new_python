from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def sortlist(head : ListNode) -> ListNode:
    # 연결 리스트 -> 파이썬 리스트 변환
    p = head
    lst : List = []

    while p :
        lst.append(p.val)
        p = p.next

    lst.sort()

    p = head
    for i in range(len(lst)):
        p.val = lst[i]
        p = p.next

    return head 



