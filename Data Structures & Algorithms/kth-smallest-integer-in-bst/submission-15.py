# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    k: list
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = []
        self.kth_smallest(root, k)
        return self.k[-1]

        
    def kth_smallest(self, root: TreeNode, k: int):
        if root == None or len(self.k) == k:
            return
        self.kth_smallest(root.left, k)
        if len(self.k) == k:
            return
        
        self.k.append(root.val)
        if len(self.k) == k:
            return
        self.kth_smallest(root.right, k)
        
        
