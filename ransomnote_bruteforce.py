# Ransom note algorithm using brute-force search
# Time complexity : O(nm) (n: num. of letters in magazine / m: num. of letters in a word)

class Solution():
    def canSpell(self, magazine, note):
        len_note = len(note)
        for w in range(len_note):
            if note[w] in magazine:
                magazine.remove(note[w])
                if (w + 1) == len_note:
                    return True
            else:
                return False


def main():
    print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
    # True
    print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
    # False
    print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'abc'))
    # True
    print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'aabc'))
    # False


if __name__ == '__main__':
    main()
