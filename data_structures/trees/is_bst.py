import math

""" Node is defined as
class Node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    if not root:
        return False

    stack = []
    node = root
    max_value = -math.inf

    while True:
        while node:
            stack.append(node)
            node = node.left

        if not stack:
            break

        node = stack.pop()

        if node.data > max_value:
            max_value = node.data
        else:
            return False

        node = node.right

    return True