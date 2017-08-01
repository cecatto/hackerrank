import sys

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""


def topView(root):
    left = []
    cur_node = root

    while cur_node.left:
        left.append(cur_node.left.data)
        cur_node = cur_node.left

    while left:
        sys.stdout.write(str(left.pop()) + ' ')

    sys.stdout.write(str(root.data) + ' ')

    cur_node = root
    while cur_node.right:
        sys.stdout.write(str(cur_node.right.data) + ' ')
        cur_node = cur_node.right
