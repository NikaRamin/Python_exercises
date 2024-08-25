class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root is None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):
        # Check if the tree is empty (i.e., no root node exists)
        if self.root is None:
            # If the tree is empty, create a new node and set it as the root
            self.root = Node(val)
        else:
            current = self.root  # Start from the root
            
            # Traverse the tree to find the correct position to insert the new value
            while True:
                if val > current.info:  # If the value is greater than the current node's value
                    if current.right:  # If the right child exists, move to the right child
                        current = current.right
                    else:
                        # If the right child does not exist, create a new node and attach it here
                        current.right = Node(val)
                        break  # Exit the loop once the new node is inserted
                elif val < current.info:  # If the value is less than the current node's value
                    if current.left:  # If the left child exists, move to the left child
                        current = current.left
                    else:
                        # If the left child does not exist, create a new node and attach it here
                        current.left = Node(val)
                        break  # Exit the loop once the new node is inserted
                else:
                    # If the value is equal to the current node's value, do nothing (no duplicates allowed)
                    break

        
        

# Create an instance of the BinarySearchTree and insert nodes as before

tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

# Output the pre-order traversal of the binary tree
preOrder(tree.root)
