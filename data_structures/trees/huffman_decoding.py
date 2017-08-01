class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None


def decodeHuff(root , s):
    decoded_str = ''
    node = root

    for c in s:
        if node.left or node.right:
            if c == '0':
                node = node.left
            else:
                node = node.right

            if node.left or node.right:
                continue

        decoded_str += node.data
        node = root

    print(decoded_str)


root = Node(5, None)
a = Node(3, 'A')
internal = Node(2, None)
b = Node(1, 'B')
c = Node(1, 'C')

root.right = a
root.left = internal
internal.left = b
internal.right = c

decodeHuff(root, '1001011')