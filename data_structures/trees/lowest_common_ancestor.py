class Node:
    def __init__(self, data):
        self.data=data
        self.left = None
        self.right = None

def lca(root , v1 , v2):

    if root.data < v1 and root.data < v2:
        return lca(root.right, v1, v2)

    if root.data > v1 and root.data > v2:
        return lca(root.left, v1, v2)

    return root

#      4
#    /   \
#   2     7
#  / \   /
# 1   3 6
#      /
#     5

four = Node(4)
two = Node(2)
one = Node(1)
three = Node(3)
seven = Node(7)
six = Node(6)
five = Node(5)

four.left = two
two.left = one
two.right = three
four.right = seven
seven.left = six
six.left = five

print(lca(four, 1, 7).data)