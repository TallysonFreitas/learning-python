class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")

def insert(tree: TreeNode, value: int):
    if tree is None:
        return TreeNode(value)
    else:
        if tree.data > value:
            tree.left = insert(tree.left, value)
        elif tree.data < value:
            tree.right = insert(tree.right, value)
    return tree


root = TreeNode(10)
nodeA = TreeNode(5)
nodeB = TreeNode(15)
nodeC = TreeNode(3)
nodeD = TreeNode(7)
nodeE = TreeNode(13)
nodeF = TreeNode(19)
nodeG = TreeNode(17)

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Test
print("root.right.left.data:", root.right.left.data)

#Python


# Traverse
pre_order_traversal(root)
print('\n')
inOrderTraversal(root)
print('\n')
postOrderTraversal(root)



insert(root, 50)
print('\n')
inOrderTraversal(root)
