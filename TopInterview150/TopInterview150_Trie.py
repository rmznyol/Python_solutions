# 208. Implement Trie (Prefix Tree)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_char = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_char = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end_char        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True       

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
###############################################################
#211. Design Add and Search Words Data Structure
class TrieNode:
    def __init__(self, val) -> None:
        # example children value: Node for quick checkups
        self.val = val
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.children = {}

    def addWord(self, word: str) -> None:
        curr = self
        for i, char in enumerate(word):
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
            curr.is_end = True if i == len(word) - 1 else curr.is_end

    def search(self, word: str,curr = None) -> bool:
        curr = curr if curr else self
        if len(word) == 1:
            if word[0] == '.':
                for child in curr.children:
                    if curr.children[child].is_end:
                        return True
            elif word[0] in curr.children and curr.children[word[0]].is_end:
                return True
            return False
        if word[0] == '.':
            for child in curr.children:
                if self.search(word[1:],curr.children[child]):
                    return True
        if word[0] in curr.children:
            return self.search(word[1:],curr.children[word[0]])
        else:
            return False
#################################################