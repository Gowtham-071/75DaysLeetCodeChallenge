from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        mp = {}

        def dfs(curr):
            if curr in mp:
                return mp[curr]

            copy = Node(curr.val)
            mp[curr] = copy

            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)