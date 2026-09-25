# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []
        stack1 = [p]
        stack2 = [q]
        if not p:
            tree1 = []
        if not q:
            tree2 = []

        while stack1:
            node = stack1.pop()
            if not node:
                tree1.append(None)
                continue
            tree1.append(node.val)
            stack1.append(node.right)
            stack1.append(node.left)
        while stack2:
            node = stack2.pop()
            if not node:
                tree2.append(None)
                continue
            tree2.append(node.val)
            stack2.append(node.right)
            stack2.append(node.left)

        print (tree1, tree2)
        if tree1 == tree2:
            return True
        else:
            return False
