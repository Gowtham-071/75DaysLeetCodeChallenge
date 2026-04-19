class Solution:
    def diameterOfBinaryTree(self, root):
        self.d = 0
        
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.d = max(self.d, l + r)
            return 1 + max(l, r)
        
        dfs(root)
        return self.d