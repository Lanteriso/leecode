'''
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
示例:
输入:
[4,3,2,7,8,2,3,1]
输出:
[5,6]
'''

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        # 方案1失败,出现 超出时间限制
        # 思路 去重 排序之后得到li,遍历完整数组 not in li 得到消失的数组,结果超时了
        if nums == []:
            return []
        li = list(set(nums))  # 1.去重
        li.sort()  # 1.排序
        print(li)
        print(len(nums))
        return [i for i in range(1, len(nums)+1) if i not in li]
        '''
        # 方案2成功 执行用时: 244 ms
        # 思路 建立一个完整序例x,和缺失序例y,找出它们的差集x-y
        x = set([i for i in range(1,len(nums)+1)])
        y=set(nums)
        return list(set(x-y))

    def findDisappearedNumbers2(self, nums):
        l = []
        s = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in s:
                l.append(i)
        return l
        # 最佳达案

    def findDisappearedNumbers3(self, nums):
        li = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in li]
        # 修改方案1,问题出现在list(set(nums))会导致内部错误,原因未知
if __name__=="__main__":
    print(Solution().findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
    print(Solution().findDisappearedNumbers2(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
    print(Solution().findDisappearedNumbers3(nums=[4, 3, 2, 7, 8, 2, 3, 1]))