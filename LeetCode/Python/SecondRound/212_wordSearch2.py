class TrieNode:
    def __init__(self) -> None:
        self.adjacent = dict()
        self.isWord = False
    
    def markWord(self):
        self.isWord = True
    
    def unmarkWord(self):
        self.isWord = False

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.adjacent:
                curr.adjacent[letter] = TrieNode()
            curr = curr.adjacent[letter]
        curr.markWord()

class Solution:
    def findWords(self, board, words):
        
        ans = []
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie.root.adjacent:
                    self.dfs(row, col, board, trie.root, ans, "")
        
        return ans

    def dfs(self, row, col, board, trieNode, ans, word):
        
        if trieNode.isWord:
            ans.append(word)
            trieNode.unmarkWord()

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or not trieNode or board[row][col] == "#":
            return
        
        ch = board[row][col]
        if ch in trieNode.adjacent:
            board[row][col] = "#"
            trieNode = trieNode.adjacent[ch]
            self.dfs(row + 1, col, board, trieNode, ans, word + ch)
            self.dfs(row - 1, col, board, trieNode, ans, word + ch)
            self.dfs(row, col + 1, board, trieNode, ans, word + ch)
            self.dfs(row, col - 1, board, trieNode, ans, word + ch)
            board[row][col] = ch

