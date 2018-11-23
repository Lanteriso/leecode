'''
自除数 是指可以被它包含的每一位数除尽的数。
例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
还有，自除数不允许包含 0 。
给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。
示例 1：
输入：
上边界left = 1, 下边界right = 22
输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
注意：
每个输入参数的边界满足 1 <= left <= right <= 10000。
'''
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        g =0
        t =[]
        for i in range(left,right+1):#所有的数
            if "0" not in str(i):#没有零的数
                for j in range(0,len(str(i))):#遍历多位数
                    g= g + i % int(str(i)[j])#多位数自除后相加
                if g == 0 :#结果不等于零时说明不是自除数
                    t.append(i)#把自除数添加到列表
                g = 0#统计归零
        return t#返回结果
print(Solution().selfDividingNumbers(left=1,right=22))