'''
给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。
示例 1:
输入: [1,4,3,2]
输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。
示例 1:
输入: [1,4,3,2]
输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
'''
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        nums.sort()
        nums =[nums[i] for i in range(len(nums)) if i%2==0]
        for j in nums:
            k = k + j
        print(k)
        return k

    def arrayPairSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(sum(nums[::2]))
        return sum(nums[::2])

Solution().arrayPairSum(nums=[1,4,3,2])
Solution().arrayPairSum1(nums=[1,4,3,2])