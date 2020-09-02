a = [[]]  # global list for the show and arr functions


class Tree(object):
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def insert(self, node):
        """Inserts a node.  The smaller values go to the left branch whilst the larger
        values go to the right branch.  This creates a sorted binary tree.  All nodes must be
        unique integers."""
        if self.data is None:
            self.data = node
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

    def search(self, node, ht=0, p=0):  # ht stands for height and p for position
        """Searches for the first appearance of the given node and prints the height and position."""
        if self.data == node:
            return print('Search found that node', node, 'has height', ht, 'and is in position', p)
        else:
            if hasattr(self.left, 'search'):
                self.left.search(node, ht + 1, 2 * p)
            if hasattr(self.right, 'search'):
                return self.right.search(node, ht + 1, 2 * p + 1)
        
    def rotate_self(self):
        """Used in the delete node to rotate clockwise the triangle made up of the three nodes
        comprised of the self and its two children."""
        if not hasattr(self.left, 'data'):
            self.left = Tree()
        if not hasattr(self.right, 'data'):
            self.right = Tree()
            
        self.data = self.left.data
        self.left.data = self.right.data
        self.right.data = None
        
    def rotate_left(self):
        """Used in the delete node to rotate clockwise the triangle made up of the three nodes
        comprised of the left child and its two children."""
        if not hasattr(self.left.left, 'data'):
            self.left.left = Tree()
        if not hasattr(self.left.right, 'data'):
            self.left.right = Tree()
            
        self.left.data = self.left.left.data
        self.left.left.data = self.left.right.data
        self.left.right.data = None
        
    def rotate_right(self):
        """Used in the delete node to rotate clockwise the triangle made up of the three nodes
        comprised of the right child and its two children."""
        if not hasattr(self.right.left, 'data'):
            self.right.left = Tree()
        if not hasattr(self.right.right, 'data'):
            self.right.right = Tree()
            
        self.right.data = self.right.left.data
        self.right.left.data = self.right.right.data
        self.right.right.data = None
        
    def delete(self, node):
        """Deletes the node and records None in its place.  Cannot delete the root."""
        if self.data is None:  # if the node has data None we try to rotate the triangle to move None down
            if (hasattr(self.left, 'data') and self.left.data is not None) or \
                    (hasattr(self.right, 'data') and self.right.data is not None):
                while self.data is None:
                    self.rotate_self()
        else:
            if node < self.data:
                if hasattr(self.left, 'data') and self.left.data == node:
                    # if left child is the node to be deleted then rotate the left triangle
                    self.rotate_left()
                    print('Deleted the node', node)
            else:
                if hasattr(self.right, 'data') and self.right.data == node:
                    # if right child is the node to be deleted then rotate the right triangle
                    self.rotate_right()
                    print('Deleted the node', node)
            if hasattr(self.left, 'data'):
                self.left.delete(node)  # go left
            if hasattr(self.right, 'data'):
                self.right.delete(node)  # go right

    def arr(self, ht=0):
        """The arr() function uses recursion to fill out the global list a.  This function is used in
        show() and in search()."""
        # global height
        global a

        if len(a) < ht + 1:  # add new lists (as entries in list a) when needed
            a.append([])
        if self.data is None:
            a[ht].append('N')
        else:
            a[ht].append(self.data)

        if hasattr(self, 'left') and hasattr(self.left, 'arr'):
            self.left.arr(ht + 1)
        elif self.left is None and not hasattr(self.left, 'arr') and ht + 1 < len(a):
            self.left = Tree()
            self.left.arr(ht + 1)
        if hasattr(self, 'right') and hasattr(self.right, 'arr'):
            self.right.arr(ht + 1)
        elif self.right is None and not hasattr(self.right, 'arr') and ht + 1 < len(a):
            self.right = Tree()
            self.right.arr(ht + 1)

    def show(self):
        """Prints the tree in a form easily understood by humans.  'N' is used as node placeholders."""
        global a
        a = [[]]
        b = []
        d = []
        k = 0
        y = 0
        z = 2
        self.arr()

        def interesting_last_line(last_line):
            """This function makes sure that the last level of the tree has at least one integer in it."""
            e = []
            m = 0

            while m < len(last_line):
                if last_line[m] == 'N':
                    e.append(True)
                else:
                    e.append(False)
                m = m + 1
            if all(e):
                a.remove(a[-1])
                interesting_last_line(a[-1])

        interesting_last_line(a[-1])

        def spaces(c):
            """This is a simple formula used to calculate number of spaces."""
            return 2 * c + 1

        while k < len(a) + 1:
            # makes the list [0, 1, 3, 7, 15, 31, ...] which is precisely the number of spaces needed between nodes
            k = k + 1
            b.append(y)
            y = spaces(y)
        k = 0

        while k < len(a) + 1:
            # makes the list [2, 5, 11, 23, 47, ...] which is precisely the number of spaces needed after back slashes
            k = k + 1
            d.append(z)
            z = spaces(z)
        b.reverse()
        d.reverse()
        for i in range(len(a)):
            string_level = ''
            branch_level = ''
            count = 0
            for j in a[i]:
                count = count + 1
                string_level = string_level + str(j) + b[i] * ' '
                if i < len(a) - 1:
                    branch_level = branch_level + '|' + b[i + 2] * ' ' + '\\' + d[i + 2] * ' '
            print(string_level)
            if i < len(a) - 1:
                print(branch_level)


root = Tree()
root.insert(5)
root.insert(10)
root.insert(4)
root.insert(8)
root.insert(3)
root.insert(7)
root.insert(2)
root.insert(1)
root.insert(6)
root.insert(9)
root.insert(11)
root.insert(12)
root.insert(13)
root.show()
root.delete(10)
root.delete(1)
root.delete(11)
root.delete(6)
root.show()
root.delete(2)
root.delete(7)
root.delete(9)
root.delete(13)
root.show()
root.search(5)
root.search(11)
root.search(9)
