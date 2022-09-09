class TreeComparator(object):

    def compare_tree(self, node1, node2):
        if not node1 or not node2:
            return node1 == node2

        if node1.data is not node2.data:
            return False

        return self.compare_tree(node1.leftChild, node2.leftChild) and self.compare_tree(node1.rightChild,
                                                                                         node2.rightChild)


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
        else:
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.rightChild:
            return self.get_max(node.rightChild)

        return node.data
        # logic 2
        actual = self.root
        while actual.rightChild is not None:
            actual = actual.rightChild

        return actual.data

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.leftChild:
            return self.get_min(node.leftChild)

        return node.data

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)
            print("------")
            self.traverse_pre_order(self.root)
            print("------")
            self.traverse_post_order(self.root)

    def traverse_in_order(self, node):
        if node.leftChild:
            self.traverse_in_order(node.leftChild)

        print('%s' % node.data)

        if node.rightChild:
            self.traverse_in_order(node.rightChild)

    def traverse_pre_order(self, node):
        print('%s' % node.data)

        if node.leftChild:
            self.traverse_pre_order(node.leftChild)

        if node.rightChild:
            self.traverse_pre_order(node.rightChild)

    def traverse_post_order(self, node):
        if node.leftChild:
            self.traverse_post_order(node.leftChild)

        if node.rightChild:
            self.traverse_post_order(node.rightChild)

        print('%s' % node.data)

    def remove_node(self, data, node):
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.leftChild)

        elif data > node.data:
            self.remove_node(data, node.rightChild)

        else:
            if node.leftChild is None and node.rightChild is None:
                print("Remove a leaf node...%d" % node.data)
                parent = node.parent

                if parent is not None and parent.leftChild == node:
                    parent.leftChild = None
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = None

                if parent is None:
                    self.root = None

                del node

            elif node.leftChild is None and node.rightChild is not None:
                print("Remove a node with single right child")
                parent = node.parent
                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild

                else:
                    self.root = node.rightChild

                node.rightChild.parent = parent
                del node

            elif node.rightChild is None and node.leftChild is not None:
                print("Remove a node with single left child")
                parent = node.parent
                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild

                else:
                    self.root = node.rightChild

                node.lefttChild.parent = parent
                del node

            else:
                print("Removing node with two children")

                predecessor = self.get_predecessor(node.leftChild)
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.rightChild:
            return self.get_predecessor(node.rightChild)
        return node

    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)


bst = BinarySearchTree()
bst.insert(12)
bst.insert(4)
bst.insert(1)
bst.insert(8)
bst.insert(20)
bst.insert(16)
bst.insert(27)

bst1 = BinarySearchTree()
bst1.insert(12)
bst1.insert(4)
bst1.insert(1)
bst1.insert(8)
bst1.insert(20)
bst1.insert(16)
bst1.insert(27)

comp = TreeComparator()
print(comp.compare_tree(bst.root,bst1.root))
