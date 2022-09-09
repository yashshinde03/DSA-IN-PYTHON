class TreeComparator(object):

    def compare_tree(self, node1, node2):
        if not node1 or not node2:
            return node1 == node2

        if node1.data is not node2.data:
            return False

        return self.compare_tree(node1.left_child, node2.left_child) and self.compare_tree(node1.right_child,
                                                                                           node2.right_child)


class Node(object):

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
