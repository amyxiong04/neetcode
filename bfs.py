from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(root):
    queue = deque()

    if root:
        queue.append(root)
    
    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            current = queue.popleft()
            print(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        level += 1

node1 = TreeNode(75)
node2 = TreeNode(60)
node3 = TreeNode(100)
node4 = TreeNode(5)
node5 = TreeNode(13)

node1.left = node2
node1.right = node3
node2.left = node5
node5.left = node4

bfs(node1)