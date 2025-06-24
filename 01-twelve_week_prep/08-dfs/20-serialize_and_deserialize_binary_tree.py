# Definition for a binary tree node.
# from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree = []
        # in order traversal
        def dfs(node):
            if not node:
                # save null value
                tree.append("N") 
                return 
            # append node value            
            tree.append(str(node.val))
            # check subtrees
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(tree) # use , as delimiter

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(",") # split by delimiter
        i = 0
        def dfs():
            nonlocal i
            if values[i] == "N":
                # found null node
                i += 1
                return None
            
            node = TreeNode(int(values[i]))
            # take next node value
            i += 1
            # dfs on subtrees 
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

    # my solution:
    # def serialize(self, root):
    #     """Encodes a tree to a single string.
        
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     tree_string = ""
    #     # in order traversal
    #     def dfs(node):
    #         nonlocal tree_string
    #         if not node:
    #             tree_string += "_" + "," # , node delimiter
    #             return # save null value
            
    #         tree_string += str(node.val) + "," # , node delimiter

    #         # check subtrees
    #         dfs(node.left)
    #         dfs(node.right)

    #         return tree_string
    #     dfs(root)
    #     print(tree_string)
    #     return tree_string


        

    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
        
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     queue = deque(data)
    #     def createTree():
    #         if not queue:
    #             return
            
    #         serialized_node = ""
            
    #          # check current node until delimiter
    #         while queue:
    #             value_to_serialize = queue.popleft()
    #             if value_to_serialize == ',':
    #                 break 
    #             serialized_node += value_to_serialize

    #         if serialized_node == '_':
    #             return
    #         # elif serialized_node == '-':
    #         #     serialized_node += queue.popleft()
    #         else:
    #             node = TreeNode(serialized_node)

    #         node.left = createTree()
    #         node.right = createTree()

    #         return node
    #     return createTree()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))