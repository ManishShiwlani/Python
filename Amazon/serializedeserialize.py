import collections
# Definition for a binary tree node.
import null as null


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def serialize(self, root):
    if root is None:
        return '[]'
    q = collections.deque([root])
    res = [root.val]
    while (q):
        node = q.popleft()
        res.append('null')
        if node.left:
            q.append(node.left)
            res[-1] = node.left.val
        res.append('null')
        if node.right:
            q.append(node.right)
            res[-1] = node.right.val
    while (res and res[-1] == 'null'):
        res.pop()
    return ','.join(map(str, res))


def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """

    if data == '[]':
        return None
    print(data)
    vals = data.split()
    print(vals[0])
    root = TreeNode(vals[0])

    return root



