"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        curr_node = self

        while curr_node is not None:
            if value < curr_node.value:
                if curr_node.left is None:
                    curr_node.left = BSTNode(value)
                    curr_node = None
                else:
                    curr_node = curr_node.left
            elif value >= curr_node.value:
                if curr_node.right is None:
                    curr_node.right = BSTNode(value)
                    curr_node = None
                else: 
                    curr_node = curr_node.right



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        curr_node = self

        while curr_node is not None:
            if curr_node.value == target:
                return True
            elif target < curr_node.value:
                if curr_node.left is None:
                    return False
                else:
                    curr_node = curr_node.left
            elif target >= curr_node.value:
                if curr_node.right is None:
                    return False
                else: 
                    curr_node = curr_node.right

    # Return the maximum value found in the tree
    def get_max(self):
        curr_node = self

        while curr_node is not None:
            if curr_node.right is not None:
                curr_node = curr_node.right
            else:
                return curr_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
# bst = BinarySearchTree(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
