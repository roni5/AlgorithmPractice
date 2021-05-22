import collections
class Codec:

    NULL = "null"
    DELIMITER = ","

    def serialize(self, root):

        if not root:
            return self.NULL + self.DELIMITER
        
        left = self.serialize(root.left)
        right = self.serialize(root.right)

        return str(root.val) + self.DELIMITER + left + right

    def deserialize(self, data):

        queue = collections.deque(data.split(self.DELIMITER))
        return self.helper(queue)
    
    def helper(self, queue):

        while queue:
            nodeVal = queue.popleft()
            if nodeVal == self.NULL:
                return None
            
            newNode = TreeNode(int(nodeVal))
            newNode.left = self.helper(queue)
            newNode.right = self.helper(queue)

            return newNode