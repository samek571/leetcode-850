# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        q, res = deque([(root, str(root.val))]), 0
        while q:
            node, val = q.popleft()
            if not node.left and not node.right:
                val = '0b' + val
                res += int(val, 2)

            if node.left:
                q.append((node.left, val + str(node.left.val)))
            if node.right:
                q.append((node.right, val + str(node.right.val)))

        return res
