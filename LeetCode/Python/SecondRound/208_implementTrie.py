class TrieNode:
    def __init__(self, val=""):
        self.isEnd = False
        self.adjacent = [None for i in range(26)]
        self.val = val
    
    def markEnd(self):
        self.isEnd = True
    
    def unMarkEnd(self):
        self.isEnd = False

    
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    
    def getIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if word is None:
            return
        
        word = word.lower()
        currentNode = self.root
        
        for letter in word:
            index = self.getIndex(letter)
            if currentNode.adjacent[index] is None:
                currentNode.adjacent[index] = TrieNode(letter)
                print(letter)
            currentNode = currentNode.adjacent[index]
        
        currentNode.markEnd()

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return False
        
        word = word.lower()
        currentNode = self.root
        
        for letter in word:
            index = self.getIndex(letter)
            if currentNode.adjacent[index] is None:
                return False
            currentNode = currentNode.adjacent[index]
        
        if currentNode and currentNode.isEnd:
            return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        prefix = prefix.lower()
        currentStr = ""
        currentNode = self.root
        
        for letter in prefix:
            index = self.getIndex(letter)
            if currentNode.adjacent[index] is None:
                return False
            currentStr += currentNode.adjacent[index].val
            #print(currentStr)
            if currentStr == prefix:
                return True
            currentNode = currentNode.adjacent[index]
        
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)