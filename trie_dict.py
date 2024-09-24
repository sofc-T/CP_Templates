# Using a dictionary - much faster than the Trie None implementation
class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {}

            cur = cur[char]
            
        cur['end'] = ''

    def search(self, word: str) -> bool:
        cur = self.trie
        for char in word:
            if char not in cur:
                return False

            cur = cur[char]

        return 'end' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for char in prefix:
            if char not in cur:
                return False

            cur = cur[char]

        return True