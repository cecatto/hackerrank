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

class Trie(object):

    END = 'end'

    def __init__(self, root=None):
        self.root = root or Node()

    def add_words(self, words):
        for word in words:
            current_node = self.root

            for letter in word:
                if current_node.count > 1 and self.END in current_node.children:
                    return word

                current_node = current_node.add_child(letter)

            current_node.add_child(self.END)

            if current_node.count > 1:
                return word

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
words = [input().strip() for i in range(n)]
trie = Trie()

offender = trie.add_words(words)

if offender:
    print("BAD SET")
    print(offender)
else:
    print("GOOD SET")

