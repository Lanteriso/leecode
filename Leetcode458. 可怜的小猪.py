'''
有1000只水桶，其中有且只有一桶装的含有毒药，其余装的都是水。它们从外观看起来都一样。如果小猪喝了毒药，它会在15分钟内死去。
问题来了，如果需要你在一小时内，弄清楚哪只水桶含有毒药，你最少需要多少只猪？
回答这个问题，并为下列的进阶问题编写一个通用算法。
进阶:
假设有 n 只水桶，猪饮水中毒后会在 m 分钟内死亡，你需要多少猪（x）就能在 p 分钟内找出“有毒”水桶？n只水桶里有且仅有一只有毒的桶。
'''
'''
# 思路:如果只有5桶水,只要一只猪,60/15=4
# 两只猪25桶
00     01     02     03      04

10     11     12     13      14

20     21     22     23      24

30     31     32     33      34

40     41     42     43      44

#三只猪

'''
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets==1:return 0
        w = minutesToTest/minutesToDie+1
        re = 1
        while pow(w,re)<buckets:
            re+=1
        return re
if __name__=="__main__":
    print(Solution().poorPigs(buckets=1000,minutesToDie=15,minutesToTest=60))