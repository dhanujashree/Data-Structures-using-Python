class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to insert into Binary Search Tree
def insert(root, data):
    if root is None:   # Step 1 & 2
        return Node(data)

    # Step 3, 4, 5: Compare and insert recursively
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


# Traversals to check tree
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Driver code
if __name__ == "__main__":
    root = None
    n = int(input("Enter number of nodes: "))
    
    print("Enter elements:")
    for i in range(n):
        el = input().strip()   # read element as string
        root = insert(root, el)

    print("\nInorder Traversal: ")
    inorder(root)
    print("\nPreorder Traversal: ")
    preorder(root)
    print("\nPostorder Traversal: ")
    postorder(root)
