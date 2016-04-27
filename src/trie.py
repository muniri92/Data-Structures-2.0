# -*- codeing: uft-8 -*-
""""Trie Algorithm Implementation."""


class Trie(object):
    """Trie class."""

    def __init__(self):
        """Initialize the trie."""
        self.root = {}

    def insert(self, token):
        """Insert a token into the Trie."""
        if not token:
            return None
        else:
            current = self.root
            for char in token.lower():
                current = current.setdefault(char, {})
            current["$"] = "$"
            print(self.root)

    def contains(self, token):
        """"Check to see if a token is contain in the Trie."""
        current = self.root
        for char in token:
            if char in current:
                current = current[char]
            else:
                return False
        return "$" in current


if __name__ == '__main__':
    t = Trie()
    t.insert("att")
    t.insert("at")
    print(t.contains("at"))
