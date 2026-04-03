# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.fillTree(preorder,inorder)
    
    def fillTree(self, preorder: List[int], inorder:List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        mid = inorder.index(preorder[0])
        node = TreeNode(inorder[mid])
        node.left = self.fillTree(preorder[1:mid+1], inorder[:mid])
        node.right = self.fillTree(preorder[mid+1:], inorder[mid+1:])
        return node

