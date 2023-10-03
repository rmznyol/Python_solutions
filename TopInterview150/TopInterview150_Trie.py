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
# 212. Word Search II

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_trie = Trie()
        for word in words:
            word_trie.insert(word)

        m, n = len(board), len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        output = set()

        def is_safe(row,col):
            return 0 <= row < m and 0 <= col < n

        visited = set()

        def dfs(row,col,node, path):
            if node.is_end:
                output.add(path)
            
            for drow, dcol in directions:
                next_row, next_col = row + drow, col + dcol
                if is_safe(next_row,next_col) and (next_row,next_col) not in visited and board[next_row][next_col] in node.children:
                    visited.add((next_row,next_col))
                    dfs(next_row,next_col,
                        node.children[board[next_row][next_col]],
                        path + board[next_row][next_col])
                    # if not removed then the visited spot will appear in the next iteration of the foor loop
                    visited.remove((next_row,next_col))
        # print(word_trie.root.children)
        for row in range(m):
            for col in range(n):
                if board[row][col] in word_trie.root.children:
                    visited.add((row,col))
                    dfs(row,col,word_trie.root.children[board[row][col]],board[row][col])
                    visited.remove((row,col))
        return list(output)