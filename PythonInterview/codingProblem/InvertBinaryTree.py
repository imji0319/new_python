'''
중앙을 기준으로 이진 트리 반전
'''

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root : TreeNode) -> TreeNode:
    if root :
        root.self, root.right = invertTree(root.right), invertTree(root.left)
        return root
    return None

import collections
# 반복구조 bfs : TOP-BOTTOM
def invertTree2(root : TreeNode) -> TreeNode:
    queue = collections.deque([root])

    while queue :
        node = queue.popleft()

        # 부모 노드부터 하향식 스왑
        if node :
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)

    return queue

# 반복구조 DFS
def invertTree3(root : TreeNode) -> TreeNode:
    stack = collections.deque([root])

    while stack :
        node = stack.pop()

        if node :
            node.left, node.right = node.right, node.left

        stack.append(node.left)
        stack.append(node.right)

    return stack

# 반복 구조로 DFS 후위 순회
def invertTree4(root : TreeNode) -> TreeNode:
    stack = collections.deque([root])

    while stack :
        node = stack.pop()

        if node :
            stack.append(node.left)
            stack.append(node.right)

            node.left, node.right = node.right, node.left

    return stack



if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    lnode = root.left
    rnode = root.right
    lnode.left = TreeNode(1)
    lnode.right = TreeNode(3)
    rnode.left = TreeNode(6)
    rnode.right = TreeNode(9)


