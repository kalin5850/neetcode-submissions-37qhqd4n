# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder_dfs(root, result):
            if root == None:
                return result
            inorder_dfs(root.left, result)
            result.append(root.val)
            inorder_dfs(root.right, result)

            return result
        
        result = inorder_dfs(root, [])
        return result[k - 1]