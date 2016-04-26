# -*- codeing: uft-8 -*-
""""Trie Algorithm Implementation."""


class Trie(object):
    """Trie class."""

    def __init__(self):
        """Initialize the trie."""
        self.root = {"*": ["$"]}

    def insert(self, token):
        """Insert a token into the Trie."""
        current = token[0]
        if current in self.root:
            count = 0

            # self.root[current] =
        elif len(token) != 1:
            self.root["*"] = {current: token[1]}
            self.insert(token)

            self.root["*"].update({"t": "$"})
        else:  # Empty and a case of one
            self.root["*"] = {current: "$"}
            # self.root["*"] = {"y": "$"}
            print(self.root)


if __name__ == '__main__':
    t = Trie()
    t.insert("at")
