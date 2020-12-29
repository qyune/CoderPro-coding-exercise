# Is a valid binary search tree?
# Time complexity : O(n)
# Space complexity : O(n)

class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def _isValidBSTHelper(self, n, low, high):
        """
        :param n: node
        :param low: low boundary
        :param high: high boundary
        :return: True of False
        """
        if not n:
            return True

        val = n.val
        if ((val > low and val < high) and
                self._isValidBSTHelper(n.left, low, n.val) and
                self._isValidBSTHelper(n.right, n.val, high)):
            return True
        else:
            return False

    def isValidBST(self, n):
        return self._isValidBSTHelper(n, float('-inf'), float('inf'))


def main():
    #    5
    #   / \
    #  4   7
    node = Node(5)
    node.left = Node(4)
    node.right = Node(7)
    print(Solution().isValidBST(node))
    # True

    #   5
    #  / \
    # 4   7
    #    /
    #   2
    node = Node(5)
    node.left = Node(4)
    node.right = Node(7)
    node.right.left = Node(2)
    print(Solution().isValidBST(node))
    # False

    #       30
    #     /    \
    #    25     35
    #    / \    / \
    #  21   29 33   36
    node = Node(30)
    node.left = Node(25)
    node.right = Node(35)
    node.left.left = Node(21)
    node.left.right = Node(29)
    node.right.left = Node(33)
    node.right.right = Node(36)
    print(Solution().isValidBST(node))
    # True


if __name__ == '__main__':
    main()
