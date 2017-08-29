class Node(object):
    __slots__ = ['letter', 'children', 'count']

    def __init__(self, letter=None):
        self.letter = None
        self.children = dict()
        self.count = 0

        if letter:
            self.set_letter(letter)

    def set_letter(self, letter):
        if not self.letter:
            self.letter = letter
        else:
            if letter != self.letter:
                raise Exception("You cannot change a node's letter!")

        self.count += 1

    def add_child(self, letter):
        child = self.children.get(letter)
        if child:
            child.count += 1
        else:
            child = Node(letter)
            self.children[letter] = child

        return child

class ContactsTrie(object):

    def __init__(self, root=None):
        self.root = root or Node()

    def add_word(self, word):
        current_node = self.root

        for letter in word:
            current_node = current_node.add_child(letter)

    def count_prefix(self, prefix):
        current_node = self.root

        for letter in prefix:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                return 0

        return current_node.count


# MAIN
n = int(input().strip())
trie = ContactsTrie()

for i in range(n):
    cmd, word = input().strip().split(' ')

    if cmd == 'add':
        trie.add_word(word)

    else:
        print(trie.count_prefix(word))


# DICT APPROACH
#
# _end = '_end_'
#
# def add_trie(root, *words):
#     for word in words:
#         current_dict = root
#
#         for letter in word:
#             current_dict = current_dict.setdefault(letter, {})
#
#         current_dict[_end] = _end
#
#     return root
#
# def in_trie(root, word):
#     """
#     Is not being used for this problem but will keep it.
#     :param root:
#     :param word:
#     :return:
#     """
#     current_dict = root
#
#     for letter in word:
#         if letter not in current_dict:
#             return False
#
#         current_dict = current_dict[letter]
#
#     return _end in current_dict
#
# def count_in_trie(root, partial):
#     current_dict = root
#
#     for letter in partial:
#         if letter not in current_dict:
#             return 0
#
#         current_dict = current_dict[letter]
#
#     count = 0
#     queue = [current_dict]
#
#     while queue:
#         current_dict = queue.pop(0)
#
#         for key in current_dict.keys():
#             if key == _end:
#                 count += 1
#                 continue
#
#             queue.append(current_dict[key])
#
#     return count

# MAIN
# n = int(input().strip())
# root = dict()
#
# for i in range(n):
#     cmd, word = input().strip().split(' ')
#
#     if cmd == 'add':
#         add_trie(root, word)
#
#     else:
#         print(count_in_trie(root, word))