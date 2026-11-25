class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()    
    
    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def _find(self, node, word, idx):
        curr = node
        
        for i in range(idx, len(word)):
            ch = word[i]
            if ch == '.':
                for _, child in curr.children.items():
                    if self._find(child, word, i + 1):
                        return True
                return False
            else:
                if ch not in curr.children:
                    return False
                curr = curr.children[ch]
        
        return curr is not None and curr.is_end

    def search(self, word: str) -> bool:
        curr = self.root
        return self._find(curr, word, 0)