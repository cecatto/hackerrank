import sys

class Node:
    def __init__(self, data):
        self.data=data
        self.left = None
        self.right = None

def print_tree(root):
    # if not root: return
    #
    # print_tree(root.left)
    # sys.stdout.write(str(root.data) + ' ')
    # print_tree(root.right)

    stack = []
    node = root

    while True:
        while node:
            stack.append(node)
            node = node.left

        if not stack:
            break

        node = stack.pop()
        sys.stdout.write(str(node.data) + ' ')
        node = node.right

def swap_nodes(root, k, height):
    queue = [root]
    cur_k = 1

    while cur_k < height:
        for _ in range(k):
            if cur_k % k != 0:
                for _ in range(len(queue)):
                    cur_node = queue.pop(0)
                    if cur_node.left: queue.append(cur_node.left)
                    if cur_node.right: queue.append(cur_node.right)
            cur_k += 1

        for _ in range(len(queue)):
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

def levelOrder(root):
    queue = [root]
    level = 1

    while queue:
        cur_node = queue.pop(0)
        level += 1
        # sys.stdout.write(str(cur_node.data) + ' ')

        if cur_node.left: queue.append(cur_node.left)
        if cur_node.right: queue.append(cur_node.right)

    return level

# main
root = Node(1)

n = int(input().strip())
queue = [root]

for _ in range(n):
    a, b = map(int, input().strip().split(' '))
    cur_node = queue.pop(0)

    if a > -1:
        left = Node(a)
        cur_node.left = left
        queue.append(left)
    if b > -1:
        right = Node(b)
        cur_node.right = right
        queue.append(right)

t = int(input().strip())
for _ in range(t):
    k = int(input().strip())
    swap_nodes(root, k, levelOrder(root))
    print_tree(root)
    sys.stdout.write('\n')


