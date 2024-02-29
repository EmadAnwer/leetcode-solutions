# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def oddEvenTree(root, level=0, lst=None):
            if lst is None:
                lst = []
            if not root:
                return True
            if level >= len(lst):
                lst.append([])
            if level % 2 == 0:
                if root.val % 2 == 0:
                    return False
                if lst[level] and root.val >= lst[level].pop():
                    return False
            else:
                if root.val % 2 != 0:
                    return False
                if lst[level] and root.val <= lst[level].pop():
                    return False
            lst[level].append(root.val)
            return oddEvenTree(root.right, level + 1, lst) and oddEvenTree(
                root.left, level + 1, lst
            )

        return oddEvenTree(root)


tree = TreeNode(
    1,
    TreeNode(
        10,
        TreeNode(3, TreeNode(12), TreeNode(8)),
    ),
    TreeNode(
        4,
        TreeNode(7, TreeNode(6)),
        TreeNode(9, right=TreeNode(2)),
    ),
)


list = []


def print_tree(root, level=0):
    if root:
        if len(list) == level:
            list.append([])
        list[level].append(root.val)
        print_tree(root.right, level + 1)
        print_tree(root.left, level + 1)


print_tree(tree)
print(list)

s = Solution()

print(s.isEvenOddTree(tree))
