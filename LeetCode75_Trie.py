# 208. Implement Trie (Prefix Tree)

class TrieNode:
    def __init__(self, val) -> None:
        # example children value: Node for quick checkups
        self.val = val
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        curr = self
        for i, char in enumerate(word):
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
            curr.is_end = True if i == len(word) - 1 else curr.is_end


    def search(self, word: str) -> bool:
        curr = self
        for i, char in enumerate(word):
            if curr := curr.children.get(char):
                if i == len(word) - 1 and curr.is_end == True:
                    return True
            else:
                return False
        return False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for i, char in enumerate(prefix):
            if curr := curr.children.get(char):
                if i == len(prefix) - 1:
                    return True
            else:
                return False
        return False
########################################################################
# 1268. Search Suggestions System

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #important point is that list is getting shorter, no need to search through the products all over again every time? That is not true 
        l=len(searchWord)
        results=[]
        products.sort()
        for i in range(l):
            temp=[]
            for word in products:
                if searchWord[0:i+1]==word[0:i+1]:
                    temp.append(word)
            products=temp
            results.append(products[:min(3,len(products))])
        return results