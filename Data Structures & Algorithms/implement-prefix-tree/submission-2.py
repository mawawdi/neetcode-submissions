class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def _find(self, word: str):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return None
            curr = curr.children[ch]
        return curr

    def search(self, word: str) -> bool:
        res = self._find(word)
        return res is not None and res.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None
        