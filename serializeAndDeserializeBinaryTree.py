# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# CAN USE EITHER LEVEL ORDER TRAVERSAL, PRE-ORDER OR POSTORDER.
# CAN I USE INORDER?? MAYBE NOT.


class Codec:
    idx = 0
    def serialize_tree(self, node):
        serial = ""
        if not node:
            return "null,"
        else:
            serial += str(node.val) + ","
            serial += self.serialize_tree(node.left)
            serial += self.serialize_tree(node.right)
        
        return serial
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        s = self.serialize_tree(root)
        # print(s)
        return s[:-1]

    def deserialize_tree(self, data):
        
        if data[self.idx] == 'null':
            self.idx += 1
            return None
        else:
            node = TreeNode(int(data[self.idx]))
            self.idx += 1
            node.left = self.deserialize_tree(data)
            node.right = self.deserialize_tree(data)
            return node
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(',')
        # print(nodes)
        return self.deserialize_tree(nodes)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
