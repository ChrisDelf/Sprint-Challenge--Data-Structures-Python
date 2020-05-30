import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # iterative solution
    # Insert the given value into the tree
    # def insert(self, value):
    #
    #     current_node = self
    #            #If inserting we must a already have a tree or root.
    #     # If value less than the self.value self.left, make a new tree/node if empty, otherwise
    #     # keep going (recursion)
    #     while current_node:
    #         if current_node.value > value:
    #             if current_node.left is None:
    #                 current_node.left = BinarySearchTree(value)
    #                 return
    #             current_node = current_node.left
    #
    #
    #
    #
    #     # if value greater than or equal to then go right, make new tree/node if empty, otherwise
    #     #keep going
    #         elif current_node.value <= value:
    #             if current_node.right is None:
    #                 current_node.right = BinarySearchTree(value)
    #                 return
    #             current_node = current_node.right
    # recursive solution
    def insert(self, value):
            if value > self.value:
                if self.right is not None:
                    self.right.insert(value)
                else:
                    self.right = BinarySearchTree(value)
            else:
                if self.left is not None:
                    self.left.insert(value)
                else:
                    self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    # iterative
    # def contains(self, target):
    #     current_node = self
    #
    #     # if target = self.value, otherwise
    #     # go left or right
    #     while current_node:
    #         if target == current_node.value:
    #             return True
    #         elif target > current_node.value:
    #             if current_node.right is None:
    #                 return False
    #             current_node = current_node.right
    #         elif target < current_node.value:
    #             if current_node.left is None:
    #                 return False
    #             current_node = current_node.left
    # recursive solution
    def contains(self, target):
            if target == self.value:
                return True
            if target > self.value and self.right is not None:
                return self.right.contains(target)
            elif target < self.value and self.left is not None:
                return self.left.contains(target)
            else:
                return False


    # Return the maximum value found in the tree
    # iterative solution
    # def get_max(self):
    #     # if right exists, got right
    #     # otherwise return self.value
    #     current_node = self
    #     while current_node.right is not None:
    #
    #
    #             current_node = current_node.right
    #     return current_node.value
    # recursive solution
    def get_max(self):
            if self.right is not None:
                return self.right.get_max()
            else:
                return self.value



    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        current_node = self
        cb(current_node.value)
        if current_node.left is not None:
            current_node.left.for_each(cb)
        if current_node.right is not None:
            current_node.right.for_each(cb)
duplicates = []
binary_tree = BinarySearchTree(names_1[0])
for name in names_1:
    binary_tree.insert(name)
for name in names_2:
    if binary_tree.contains(name):
            duplicates.append(name)
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
