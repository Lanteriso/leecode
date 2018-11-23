'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false
'''

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_map = {}
        for i in range(len(nums)):
            if nums[i] in num_map and i - num_map[nums[i]]<=k:
                return True
            else:
                num_map[nums[i]] =i
        return False




    def containsNearbyDuplicate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if len(nums) == len(set(nums)):
            return False
        elif len(nums) <= k:
            return True
        for i in range(k, len(nums), 1):
            if len(set(nums[i - k:i + 1])) <= k:
                return True
        return False
print(Solution().containsNearbyDuplicate(nums=[1, 4, 3, 1], k=3))
print(Solution().containsNearbyDuplicate1(nums = [1,2,3,1], k = 3))