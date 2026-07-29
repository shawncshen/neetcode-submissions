# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #brute force, check 1 by 1
        if p is None and q is None:
            return True
        
        if p is None and q != None:
            return False
        if p != None and q == None:
            return False
        if p.val != q.val:
            return False
        left_same = self.isSameTree(p.left, q.left) #recursion?
        right_same = self.isSameTree(p.right, q.right)

        return left_same and right_same
