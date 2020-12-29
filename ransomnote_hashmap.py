# Ransom note algorithm using hashmap

from collections import defaultdict


class Solution():
    def canSpell(self, magazine, note):
        letters = defaultdict(int)
        # letters = {i : 0 for i in magazine} # <-- cannot handle letters not in magazine
        for c in magazine:
            letters[c] += 1

        for c in note:
            if letters[c] <= 0:
                return False
            else:
                letters[c] -= 1
        return True


def main():
    print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
    # True
    print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
    # False


if __name__ == '__main__':
    main()


"""
-------- Usage of <defaultdict> --------

>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> d.items()
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
"""


