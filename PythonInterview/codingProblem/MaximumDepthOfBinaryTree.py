'''
트리 : 순환 구조를 가지고 있지 않은 그래프
이진 트리 : 모든 노드의 차수가 2개 이하인 트리, 즉 왼쪽, 오른쪽 최대 2개의 자식을 가지는 매우 단순한 형태.
'''

# 이진 트리의 최대 깊이를 구하라
import collections

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root : TreeNode) -> int :
    if root is None :
        return 0

    queue = collections.deque([root])

    depth = 0

    while queue :
        depth += 1

        # 큐 연산 추출 노드의 자식 노드 삽입
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)


    # BFS 반복횟수 == 깊이
    return depth



if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    lnode = root.left
    rnode = root.right
    lnode.left = None
    lnode.right = None
    rnode.left = TreeNode(15)
    rnode.right = TreeNode(7)


    print(maxDepth(root))



