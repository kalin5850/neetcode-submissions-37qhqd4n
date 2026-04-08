# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.cur = root
        self.stack = []
        self.res = []

        while self.cur or self.stack:
            if self.cur:
                self.stack.append(self.cur)
                self.cur = self.cur.left
            else:
                self.cur = self.stack.pop()
                self.res.append(self.cur.val)
                self.cur = self.cur.right

    def next(self) -> int:
        if self.hasNext():
            return self.res.pop(0)
        

    def hasNext(self) -> bool:
        return len(self.res) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()