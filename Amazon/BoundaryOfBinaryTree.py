import null


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Node:
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def leftBoundary(node):
            if not node or (node.left is None and node.right is None):
                return
            b.append(node.val)
            if node.left:
                leftBoundary(node.left)
            else:
                leftBoundary(node.right)

        def leaves(node):
            if not node:
                return
            leaves(node.left)
            if node != root and node.left is None and node.right is None:
                b.append(node.val)

            leaves(node.right)

        def rightBoundary(node):
            if not node:
                return
            if node.right:
                rightBoundary(node.right)
            elif node.left:
                rightBoundary(node.left)
            else:  # not node.right and not node.left
                return
            b.append(node.val)
        # base case
        if not root: return []
        b = [root.val]
        leftBoundary(root.left)
        leaves(root)
        rightBoundary(root.right)
        return b


if __name__ == "__main__":
    s = Node()
    root = [1,null,2,3,4]
    s.boundaryOfBinaryTree(root)
