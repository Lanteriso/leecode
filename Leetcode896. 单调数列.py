'''
如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 true，否则返回 false。



示例 1：

输入：[1,2,2,3]
输出：true
示例 2：

输入：[6,5,4,4]
输出：true
示例 3：

输入：[1,3,2]
输出：false
示例 4：

输入：[1,2,4,5]
输出：true
示例 5：

输入：[1,1,1]
输出：true
'''
import operator
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        return sorted(A)==A or A==sorted(A, reverse=True)
        #return operator.eq(sorted(A), A) or operator.eq(A, sorted(A, reverse=True))
        # A升 降 排序后和A比较



if __name__=="__main__":
    print(Solution().isMonotonic(A=[1,2,2,3]))