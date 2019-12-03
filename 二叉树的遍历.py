class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def isSearchTree(root: Node) -> bool:
    def helper(n=root, lower=float("-inf"), upper=float("inf")) -> bool:
        if not n: return True
        if n.val <= lower or n.val >= upper: return False
        if not helper(root.left, lower, n.val): return False
        if not helper(root.right, root.val, upper): return False
        return True
    return helper()

def preorder(root: Node):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def preorder1(root: Node):
    stack = [root]
    while stack:
        cur = stack.pop()
        print(cur.val)
        stack.append(cur.right)
        stack.append(cur.left)
    
def inorder(root: Node):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def inorder1(root: Node):
    stack, p = [], root
    while stack or p:
        while p:
            stack.append(p)
            p = p.left
        p = stack.pop()
        print(p.val)
        p = p.right

def postorder(root: Node):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def postorder1(root: Node) -> [int]:
    stack, res = [root], []
    while stack:
        cur = stack.pop()            
        if cur:
            res.append(cur.val)
            stack.append(cur.left)
            stack.append(cur.right)
    return res[::-1]

