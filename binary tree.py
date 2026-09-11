class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_nodes(root):
    # If tree is empty
    if root is None:
        return 0

    # Count current node + left subtree + right subtree
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# Example binary tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

print("Total number of nodes:", count_nodes(root))
