# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        result = []
        if root != None:
            q.append(root)
        while len(q) > 0:
            count = 0
            for i in range(len(q)):
                curr = q.popleft()
                if count != 1:
                    result.append(curr.val)
                    count += 1
                if curr.right != None:
                    q.append(curr.right)
                if curr.left != None:
                    q.append(curr.left)
        
        return result