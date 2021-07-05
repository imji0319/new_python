# 연결리스트를 삽입 정렬로 정렬하라

from typing import List
# 연결리스트
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def insertionSortList(head : ListNode) -> ListNode:
    cur = present = ListNode(None)

    while head:
        while cur.next and cur.next.val < head.val :
            cur = cur.next

        cur.next, head.next, head = head, cur.next, head.next

        cur = present
    return cur.next


# 삽입 정렬 비교 조건 개선
def insertionSortList(head : ListNode) -> ListNode:

    cur = present = ListNode(0)

    while head:
        while cur.next and cur.next.val < head.val :
            cur = cur.next
        cur.next , head.next, head = head, cur.next, head.next

        # 필요한 경우에만 cur 포인트가 되돌아가도록 처리
        if head and cur.val > head.val :
            cur = present

    return present.next

