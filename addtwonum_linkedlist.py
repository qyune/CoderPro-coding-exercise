"""
Add two numbers as linked list
"""


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        # Reculsive
        # return self.addTwoNumbersReculsive(l1, l2, 0)
        # Iterative
        return self.addTwoNumbersIterative(l1, l2)

    def addTwoNumbersReculsive(self, l1, l2, c):
        val = l1.val + l2.val + c
        c = val // 10
        ret = Node(val % 10)

        if l1.next is not None or l2.next is not None:
            if l1.next is None:
                l1.next = Node(0)
            if l2.next is None:
                l2.next = Node(0)
            ret.next = self.addTwoNumbersReculsive(l1.next, l2.next, c)
        elif c != 0:
            ret.next = Node(c)
        return ret

    def addTwoNumbersIterative(self, l1, l2):
        a = l1
        b = l2
        c = 0
        ret = current = None

        while a is not None or b is not None:
            val = a.val + b.val + c
            c = val // 10   # carry over
            if current is None:
                ret = current = Node(val % 10)  # mod
            else:
                current.next = Node(val % 10)   # mod
                current = current.next

            if a.next is not None or b.next is not None:
                if a.next is None:
                    a.next = Node(0)
                if b.next is None:
                    b.next = Node(0)
            elif c != 0:
                current.next = Node(c)
            a = a.next
            b = b.next
        return ret


def main():
    l1 = Node(2)
    l1.next = Node(4)
    l1.next.next = Node(3)

    l2 = Node(5)
    l2.next = Node(6)
    l2.next.next = Node(4)

    answer = Solution().addTwoNumbers(l1, l2)
    while answer:
        print(answer.val, end=' ')
        answer = answer.next


if __name__ == '__main__':
    main()
