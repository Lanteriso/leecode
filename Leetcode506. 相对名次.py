'''
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。
(注：分数越高的选手，排名越靠前。)
示例 1:
输入: [5, 4, 3, 2, 1]
输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
'''
class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # 先排序sorted,用新数组index下标 替换旧数组对应的数
        medel=["Gold Medal", "Silver Medal", "Bronze Medal"]
        newnums =sorted(nums, reverse=True)
        for i in range(len(nums)):
            j = nums.index(newnums[i])
            if i>=3:
                nums[j] =str(i+1)
            else:
                nums[j] = medel[i]
        return nums

if __name__=="__main__":
    print(Solution().findRelativeRanks(nums=[10,3,8,9,4]))