# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        result: list[list[int]] = []

        if root != None:
            q.append(root)
        
        while len(q) > 0:
            same_level: list[int] = []
            for i in range(len(q)):
                curr = q.popleft()
                same_level.append(curr.val)
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)
            result.append(same_level)
        
        return result