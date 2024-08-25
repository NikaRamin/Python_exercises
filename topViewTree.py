# Node class to define the structure of each node in the binary tree
class Node:
    def __init__(self, info): 
        self.info = info  # Value of the node
        self.left = None  # Left child of the node
        self.right = None  # Right child of the node
        self.level = None  # Level of the node (not used in this implementation)

    def __str__(self):
        return str(self.info)  # String representation of the node

# BinarySearchTree class to define the operations on the binary search tree
class BinarySearchTree:
    def __init__(self): 
        self.root = None  # Initially, the tree is empty, so root is None

    # Method to insert a value into the tree and create the necessary nodes
    def create(self, val):  
        if self.root == None:  # If the tree is empty, insert the first node as the root
            self.root = Node(val)
        else:
            current = self.root  # Start from the root
         
            while True:
                if val < current.info:  # If the value is less than the current node's value
                    if current.left:  # If there's a left child, move to the left child
                        current = current.left
                    else:  # If there's no left child, create a new node and attach it as the left child
                        current.left = Node(val)
                        break
                elif val > current.info:  # If the value is greater than the current node's value
                    if current.right:  # If there's a right child, move to the right child
                        current = current.right
                    else:  # If there's no right child, create a new node and attach it as the right child
                        current.right = Node(val)
                        break
                else:
                    break  # If the value is equal to the current node's value, do nothing (no duplicates)

"""
Node is defined as:
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

# Function to print the top view of the binary tree
def topView(root):
    if root is None:
        return
    
    # Queue to store nodes along with their horizontal distance (HD)
    queue = [(root, 0)]  # Start with the root node at horizontal distance 0
    
    # Dictionary to store the first node encountered at each horizontal distance
    hd_map = {}
    
    # Perform a level order traversal using the queue
    while queue:
        current, hd = queue.pop(0)  # Dequeue the front of the queue
        
        # If this horizontal distance is not yet seen, store the node's value
        if hd not in hd_map:
            hd_map[hd] = current.info
        
        # Enqueue the left child with its corresponding horizontal distance (HD - 1)
        if current.left:
            queue.append((current.left, hd - 1))
        
        # Enqueue the right child with its corresponding horizontal distance (HD + 1)
        if current.right:
            queue.append((current.right, hd + 1))
    
    # Print the top view, which is the nodes stored in hd_map sorted by their horizontal distance
    for key in sorted(hd_map):
        print(hd_map[key], end=' ')

# Create an instance of the BinarySearchTree
tree = BinarySearchTree()

# Read the number of nodes to be inserted in the tree
t = int(input())

# Read the values to be inserted into the tree
arr = list(map(int, input().split()))

# Insert each value into the tree
for i in range(t):
    tree.create(arr[i])

# Output the top view of the binary tree
topView(tree.root)
