'''
给定一个整数数组 A，对于每个整数 A[i]，我们可以选择任意 x 满足 -K <= x <= K，并将 x 加到 A[i] 中。
在此过程之后，我们得到一些数组 B。
返回 B 的最大值和 B 的最小值之间可能存在的最小差值。
示例 1：
输入：A = [1], K = 0 输出：0 解释：B = [1]
示例 2：
输入：A = [0,10], K = 2 输出：6 解释：B = [2,8]
示例 3：
输入：A = [1,3,6], K = 3 输出：0 解释：B = [3,3,3] 或 B = [4,4,4]
'''
class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # 因为,B 的最大值和 B 的最小值之间可能存在的最小差值,所以我们尽可能让B和B的差最小
        # 因为将 x 加到 A[i] 中 得到 B,所以B的值是A[i]+x=B,当(max(A)-max(x))-(min(A)-min(x))时,B和B的差最小
        # 因为-K <= x <= K,所以max(x)=K,min(x)=-K,于是(max(A)-max(x))-(min(A)-min(x)) 等于 (max(A)-K) - (min(A)+K)
        # 第二种情况,如果当K的值大于max(A)和min(A)中间,就是((max(A)-min(A)))/2<K时,B的最小差值可能存在0
        if ((max(A)-min(A)))/2<K:
            return 0
        else:
            return (max(A)-K) - (min(A)+K)
print(Solution().smallestRangeI(A = [0,10], K = 2))

