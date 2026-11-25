class TrieNode:
    def __init__(self):
        # Maps each character to its child TrieNode (compact and handles any alphabet)
        self.children = {}
        # Distinguishes a complete inserted word from a mere prefix path
        self.is_end = False


class PrefixTree:
    def __init__(self):
        # Root represents the empty prefix ""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            # Allocate a new node only when branching off an unseen prefix
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def _find(self, text: str):
        # Shared traversal helper: walks down the tree and returns the final node, or None
        curr = self.root
        for ch in text:
            if ch not in curr.children:
                return None
            curr = curr.children[ch]
        return curr

    def search(self, word: str) -> bool:
        node = self._find(word)
        # Path must exist AND end at a node explicitly marked as a full word
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        # Any valid path guarantees at least one inserted word has this prefix
        return self._find(prefix) is not None