from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return None

        inverted_left = self.invertTree(root.left)
        inverted_right = self.invertTree(root.right)

        root.left = inverted_right
        root.right = inverted_left

        return root