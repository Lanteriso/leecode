#-*-coding:utf-8-*-
from collections import Counter
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        counts = Counter(deck)
        values = [v for v in counts.values()]
        minCount = min(values)
        result = False
        for i in range(2, 6):
            result = all([n % i == 0 for n in values])
            if result:
                break
        print result
        return result

Solution().hasGroupsSizeX(deck=[1,1,1,2,2,2,3,3,3])

class Solution1(object):
    def hasGroupsSizeX1(self, deck):
        count = Counter(deck)
        N = len(deck)
        for X in xrange(2, N+1):
            if N % X == 0:
                if all(v % X == 0 for v in count.values()):
                    print True
                    return True
        print False
        return False
Solution1().hasGroupsSizeX1(deck=[1,1,1,2,2,2,3,3,3])


class Solution2(object):
    def hasGroupsSizeX2(self, deck):
        from fractions import gcd
        vals = Counter(deck).values()
        print reduce(gcd, vals) >= 2
        return reduce(gcd, vals) >= 2

Solution2().hasGroupsSizeX2(deck=[1,1,2,2,2,3,3,3])


