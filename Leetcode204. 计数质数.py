'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        nums = [1] * n
        nums[:2] = [0] * 2
        nums[2:n:2] = [0] * ((n - 1) // 2)
        for i in range(3, int(n ** 0.5) + 1, 2):
            if nums[i] == 1:
                nums[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)
        return sum(nums) + 1







if __name__ == "__main__":
    print(Solution().countPrimes(n=168))