# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_value = preorder[0]
        root = TreeNode(root_value)
        middle = inorder.index(root_value) #starting val of preorder
        left_inorder = inorder[:middle]
        right_inorder = inorder[middle + 1:]

        left_size = len(left_inorder)

        left_preorder = preorder[1:1 + left_size]
        right_preorder = preorder[1 + left_size:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
