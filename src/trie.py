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
        if current in self.root:  # Currently exists to a point
            count = 0

            # self.root[current] =
        elif len(token) != 1:  # Empty and multipy letters long 
            # while count != len(token):
            self.root["*"] = {current: "$"}
            self.root[current].update({"t": "$"})
            

            # self.insert(token)

            # self.root["*"] = {"y": "$"}

        else:  # Empty and a case of one
            self.root["*"] = {current: "$"}
            print(self.root)


if __name__ == '__main__':
    t = Trie()
    t.insert("at")
