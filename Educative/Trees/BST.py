class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self, val=None):
        if val is None:
            self.root = None
        else:
            self.root = Node(val)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while current:
                parent = current
                if val < current.val:
                    current = current.left
                else:
                    current = current.right
            if val < parent.val:
                parent.left = Node(val)
            else:
                parent.right = Node(val)
    
    def search(self, val):
        if self.root is None:
            return None
        
        else:
            current = self.root
            while current and current.val != val:
                if val < current.val:
                    current = current.left
                else:
                    current = current.right
        
        return None if current is None else current
    
    def delete(self, val):
        #Empty tree
        if self.root is None:
            return False
        
        #Search
        node = self.root
        parent = None
        while node and node.val != val:
            parent = node
            if val < node.val:
                node = node.left
            else:
                node = node.right
        
        #Node not found
        if node is None or node.val != val:
            return False
        #Node is the leaf
        elif node.left is None and node.right is None:
            print("Deleted node is leaf")
            if parent is None: #the node is the root
                node = None
            elif val < parent.val:
                parent.left = None
            else:
                parent.right = None
            return True
        #node has left child only
        elif node.left and node.right is None:
            print("deleted node has left child only")
            if parent is None:
                self.root = self.root.left
            elif val < parent.val:
                parent.left = node.left
            else:
                parent.right = node.left
            return True
        #node has right child only
        elif node.right and node.left is None:
            print("deleted node has right child only")
            if parent is None:
                self.root = self.root.right
            elif val < parent.val:
                parent.left = node.right
            else:
                parent.right = node.right
            return True
        #node has two children
        else:
            print("deleted node has both children")
            replaceNodeParent = node
            replaceNode = node.right
            while replaceNode.left:
                replaceNodeParent = replaceNode
                replaceNode = replaceNode.left
            
            node.val = replaceNode.val
            if replaceNode.right:
                if replaceNode.val < replaceNodeParent.val:
                    replaceNodeParent.left = replaceNode.right
                elif replaceNode.val > replaceNodeParent.val:
                    replaceNodeParent.right = replaceNode.right
            else:
                if replaceNode.val < replaceNodeParent.val:
                    replaceNodeParent.left = None
                else:
                    replaceNodeParent.right = None
            return True
        return False
        
bst = BST()
# print(bst.root.val)
bst.insert(3)
bst.insert(1)
print(bst.root.val)
print(bst.root.left.val)
print(bst.delete(3))
print(bst.root.val)