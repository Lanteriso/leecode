#-*-coding:utf-8-*-
'''
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。

所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。

说明:

给出的房屋和供暖器的数目是非负数且不会超过 25000。
给出的房屋和供暖器的位置均是非负数且不会超过10^9。
只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
所有供暖器都遵循你的半径标准，加热的半径也一样。
示例 1:

输入: [1,2,3],[2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
示例 2:

输入: [1,2,3,4],[1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
'''

# 思路二：设置一个index，来表示离house最近的heater的坐标。每次遍历house时，对于每个house，循环heater，
# 条件为，index没有到heater最后一个，且heater[index+1]与house[i]的差小于heater[index]与house[i]的差，
# 这说明，此时的index处的heater离house不是最近，index++。循环heater完成后，返回maxinx和heater[index]与house[i]的差中较大的那一个。

class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        maxidx = 0
        index = 0
        for i in range(len(houses)):
            while index + 1 < len(heaters) and (abs(heaters[index + 1] - houses[i]) <= abs(heaters[index] - houses[i])):
                index += 1
            maxidx = max(maxidx, abs(heaters[index] - houses[i]))
        return maxidx

Solution().findRadius(houses=[1,2,3,4,5,6],heaters=[1,5])