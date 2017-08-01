import sys

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def levelOrder(root):
    queue = [root]

    while queue:
        cur_node = queue.pop(0)

        sys.stdout.write(str(cur_node.data) + ' ')

        if cur_node.left: queue.append(cur_node.left)
        if cur_node.right: queue.append(cur_node.right)
