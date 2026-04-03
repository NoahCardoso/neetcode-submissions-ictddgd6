# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def dfs(root):
            if not root:
                return 0
            maxLeft = max(dfs(root.left),0)
            maxRight = max(dfs(root.right),0)

            noSplit = maxLeft + maxRight + root.val
            split = root.val + max(maxLeft,maxRight)

            self.res = max(noSplit, self.res)
            return split
        dfs(root)
        return self.res