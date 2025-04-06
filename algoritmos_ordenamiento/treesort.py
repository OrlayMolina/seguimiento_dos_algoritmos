class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def in_order(root, result):
    if root:
        in_order(root.left, result)
        result.append(root.key)
        in_order(root.right, result)

def treesort(arr):
    if not arr:
        return []
    
    root = None
    for item in arr:
        root = insert(root, item)
    
    result = []
    in_order(root, result)
    return result
