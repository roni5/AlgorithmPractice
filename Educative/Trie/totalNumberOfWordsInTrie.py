from trie import Trie

def totalWordsinTrie(root):
    result = 0

    if root.isEndWord:
        result += 1
    
    for i in range(26):
        if root.children[i] is not None:
            result += totalWordsinTrie(root.children[i])
    
    return result

trie = Trie()

keys = ["the", "a", "there", "answer", "any","by", "bye", "their","abc"]

trie = Trie()

for key in keys:
  trie.insert(key)
  
print(totalWordsinTrie(trie.root))