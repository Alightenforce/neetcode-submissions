# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depths = []
        max_length = 0
        def traverse(node, depth):
            if not node:
                return 
            if not node.left and not node.right:
                depths.append(depth)
                return
            traverse(node.left, depth + 1)          # Go down left
            traverse(node.right, depth + 1)         # Go down right

        traverse(root, depth = 1)
        if len(depths) == 0:
            return 0
        else:
            return max(depths)