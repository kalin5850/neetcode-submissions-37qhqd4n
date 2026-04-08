# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # dfs
        def dfs(root: Optional[TreeNode], res: List[int]) -> List[int]:
            if root == None:
                return res
            res.append(root.val)
            dfs(root.left, res)
            dfs(root.right, res)

            return res
        
        return dfs(root, [])