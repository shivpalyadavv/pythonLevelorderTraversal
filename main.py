# Python program to print level
# order traversal using queue

# A node structure
class Node:

    # A utility function to create a new node
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

# Iterative Method to print the
# height of a bnary tree
def printLevelOrder(root):

    # Base case
    if root is None:
        return

    # Create an empty queue
    # for level order traversal
    queue = []

    # Enqueue Root and intialize height
    queue.append(root)

    while(len(queue) > 0):

        #print front of queue and
        #remove it from queue
        print (queue[0].data)
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enque right child
        if node.right is not None:
            queue.append(node.right)

#Driver Program to test above finction
root = Node(1)
root.left = Node(2)
root.right =Node(3)
root.left.left = Node (4)
root.left.right = Node(5)

print ("Level order traversal of binary tree is -")
printLevelOrder(root)



