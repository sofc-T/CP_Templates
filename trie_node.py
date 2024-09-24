from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = defaultdict(int)

class Trie:

    def __init__(self):
        self.root =TrieNode()

    def insert(self, word: str) -> None:
        parent = self.root
        for idx in range(len(word)):
            child = ord(word[idx]) - 97
            if not parent.children[child]: 
                parent.children[child] = TrieNode()
                
            parent = parent.children[child]
            
        parent.is_end = True

    def search(self, word: str) -> bool:
        parent = self.root
        for idx in range(len(word)):
            child = ord(word[idx]) - 97
            if not parent.children[child]:
                return False
            
            parent = parent.children[child]
            
        return parent.is_end

    def startsWith(self, prefix: str) -> bool:
        parent = self.root
        for idx in range(len(prefix)):
            child = ord(prefix[idx]) - 97
            if not parent.children[child]:
                return False
            
            parent = parent.children[child]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)