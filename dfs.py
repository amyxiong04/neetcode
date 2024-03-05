class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

node1 = TreeNode(75)
node2 = TreeNode(60)
node3 = TreeNode(100)
node4 = TreeNode(5)
node5 = TreeNode(13)


node1.left = node2
node1.right = node3
node2.left = node5
node5.left = node4

inorder(node1)
print()
preorder(node1)
print()
postorder(node1)