class Solution:
    def isSameTree(self, a, b):
        if a is None and b is None:
            return True

        if a is None or b is None:
            return False

        if a.val != b.val:
            return False

        return (self.isSameTree(a.left, b.left) and
                self.isSameTree(a.right, b.right))

    def isSubtree(self, root, subRoot):
        if root is None:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        