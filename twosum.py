""" Find indexes of two elements in the pool, summed up as a target """

class Solution(object):
    def twoSumA(self, pool, target):
        l = len(pool)
        for n in range(l):
            for m in range(n + 1, l):
                res = pool[n] + pool[m]
                if res == target:
                    return [pool.index(pool[n]), pool.index(pool[m])]
        return []

    def twoSumB(self, pool, target):
        l = len(pool)
        for n in range(l):
            for m in range(l):
                if n == m:
                    continue
                else:
                    res = pool[n] + pool[m]
                if res == target:
                    return [pool.index(pool[n]), pool.index(pool[m])]
        return []

    def twoSumC(self, pool, target):
        values = {}
        for index, num in enumerate(pool):
            diff = target - num
            if diff in values:
                return [values[diff], index]
            values[num] = index


def main():
    pool = [2, 7, 11, 15]
    target = 18
    print(Solution().twoSumC(pool, target))

    # pool = []
    # target = 18
    # print(Solution().twoSumA(pool, target))


if __name__ == '__main__':
    main()
