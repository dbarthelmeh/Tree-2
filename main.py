height = 0
a = [[]]


class Tree(object):
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def insert(self, node):
        """Inserts a node.  The smaller values go to the left branch whilst the equal and larger
         values go to the right branch.  This creates a sorted binary tree."""
        if self.data is None:
            self.data = node
            print('Inserted', node)
            return
        else:
            if node < self.data:
                if self.left is None:
                    self.left = Tree()
                self.left.insert(node)
            else:
                if self.right is None:
                    self.right = Tree()
                self.right.insert(node)

    def search(self, node):
        """Searches for the first appearance of the given node and prints the position and the height."""
        global a
        a = [[]]
        self.arr()
        for i in range(len(a)):
            for j in a[i]:
                if j == node:
                    return print('Search found that', j, 'is in position', a[i].index(j), 'and has height', i)
        return print(node, 'is not found in the tree')

    def delete(self, node):
        """Deletes the node and records None in its place."""
        if self.data == node:
            self.data = None
            print('Deleted', node)
            return
        else:
            if self.data is None:  # if the node has data None we attempt to traverse down the tree
                if hasattr(self.left, 'delete'):
                    self.left.delete(node)
                if hasattr(self.right, 'delete'):
                    self.right.delete(node)
            else:
                if node < self.data:
                    if self.left is not None:
                        self.left.delete(node)
                else:
                    if self.right is not None:
                        self.right.delete(node)

    def arr(self):
        """The arr() function uses recursion to fill out the global list a.  This function is used in
        show() and in search()."""
        global height
        global a

        if len(a) < height + 1:  # add new lists (as entries in list a) when needed
            a.append([])
        a[height].append(self.data)

        if hasattr(self, 'left') and hasattr(self.left, 'arr'):
            height = height + 1
            self.left.arr()
            height = height - 1

        if hasattr(self, 'right') and hasattr(self.right, 'arr'):
            height = height + 1
            self.right.arr()
            height = height - 1

    def show(self):
        """Prints the tree in a form easily understood by humans."""
        global height
        global a
        height = 0
        a = [[]]
        self.arr()
        for i in range(len(a)):
            string_level = ''
            branch_level = ''
            count = 0
            for j in a[i]:
                count = count + 1
                string_level = string_level + str(j)
                if count % 2 == 1:
                    # the space between two numbers in a pair
                    string_level = string_level + (len(a) - i - 1) * '    ' + ' '
                else:
                    # the space between two pairs of numbers
                    string_level = string_level + (len(a) - i) * ' '
                if i < len(a) - 1:
                    branch_level = branch_level + '|' + (2 ** (len(a) - i - 2)) * ' ' + '\\ ' + (
                                2 ** (len(a) - i - 1)) * ' '
            print(string_level)
            if i < len(a) - 1:
                print(branch_level)


root = Tree()
root.insert(4)
root.insert(2)
root.insert(6)
root.insert(1)
root.insert(3)
root.insert(5)
root.insert(9)
root.insert(5)
root.show()
root.delete(6)
root.show()
root.search(5)
root.delete(5)
root.search(5)
root.delete(5)
root.search(5)
root.search(10)
root.show()
