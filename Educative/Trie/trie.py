class TrieNode:
  def __init__(self, char = ''):
    self.children = [None] * 26 #Total # of English Alphabets
    self.isEndWord = False #will be true if the node represents the end of word
    self.char = char #To store the value of a particular key
  
  #Function to mark the currentNode as Leaf
  def markAsLeaf(self):
    self.isEndWord = True
    
  #Function to unMark the currentNode as Leaf  
  def unMarkAsLeaf(self):
    self.isEndWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode() #Root node
        
    #Function to get the index of a character 't'
    def getIndex(self,t):
        return ord(t) - ord('a')
    
    #Function to insert a key in the Trie
    def insert(self,key):
        if key is None:
            return
        key = key.lower()
        currentNode = self.root
        index = 0

        #Iterate the trie with the given character index,
        #If the index points to None
        #simply create a TrieNode and go down a level
        for level in range(len(key)):
            index = self.getIndex(key[level])

            if currentNode.children[index] == None:
                currentNode.children[index] = TrieNode(key[level])
                print(key[level] + " inserted")
            
            currentNode = currentNode.children[index]
        
        #Mark the end character as leaf node
        currentNode.markAsLeaf()
        print ("'" + key + "' inserted")

        
    #Function to search a given key in Trie
    def search(self,key):
        if key is None:
            return False
        
        key = key.lower()
        currentNode = self.root
        index = 0

        #Iterate the Trie with given character index,
        #If it is None at any point then we stop and return false
        #We will return true only if we reach leafNode and have traversed the
        #Trie based on the length of the key
        for level in range(len(key)):
            index = self.getIndex(key[level])
            if currentNode.children[index] is None:
                return False
            currentNode = currentNode.children[index]
        
        if currentNode is not None and currentNode.isEndWord:
            return True

        return False 

    def hasNoChildren(self, currentNode):
        for child in currentNode.children:
            if child is not None:
                return False
        return True

    def deleteRec(self, key, currentNode, length, level):
        deletedSelf = False

        if currentNode is None:
            print("Key does not exist")
            return deletedSelf
        
        #Base Case: If we have reached at the node which points to the alphabet at the end of the key.
        if level == length:
            #If there are no nodes ahead of this node in this path
            #Then we can delete this node
            if self.hasNoChildren(currentNode):
                currentNode = None
                deletedSelf = True
            
            #If there are nodes ahead of currentNode in this path 
            #Then we cannot delete currentNode. We simply unmark this as leaf
            else:
                currentNode.unMarkAsLeaf()
                deletedSelf = False
        else:
            childNode = currentNode.children[self.getIndex(key[level])]
            childDeleted = self.deleteRec(key, childNode, length, level + 1)
            if childDeleted:
                 #Making children pointer also None: since child is deleted
                currentNode.children[self.getIndex(key[level])] = None
                if currentNode.isEndWord:
                    deletedSelf = False
                
                #If childNode is deleted but if currentNode has more children then currentNode must be part of another key
                #So, we cannot delete currenNode
                elif self.hasNoChildren(currentNode) == False:
                    deletedSelf = False

                 #Else we can delete currentNode
                else:
                    currentNode = None
                    deletedSelf = True
            else:
                deletedSelf = False


        return deletedSelf
    
    #Function to delete given key from Trie
    def delete(self,key):
        if self.root is None or key is None:
            return
        self.deleteRec(key, self.root, len(key), 0)

    
#     # Input keys (use only 'a' through 'z')
# keys = ["the", "a", "there", "answer", "any",
#                  "by", "bye", "their","abc"]
# output = ["Not present in trie", "Present in trie"]

# t = Trie()
# print("Keys to insert: ")
# print(keys)

# #Construct Trie
# for i in range(len(keys)):
#   t.insert(keys[i])