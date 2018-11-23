'''
给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。
如果没有两个连续的 1，返回 0 。
示例 1：
输入：22
输出：2
解释：
22 的二进制是 0b10110 。
在 22 的二进制表示中，有三个 1，组成两对连续的 1 。
第一对连续的 1 中，两个 1 之间的距离为 2 。
第二对连续的 1 中，两个 1 之间的距离为 1 。
答案取两个距离之中最大的，也就是 2 。
示例 2：
输入：5
输出：2
解释：
5 的二进制是 0b101 。
示例 3：
输入：6
输出：1
解释：
6 的二进制是 0b110 。
示例 4：
输入：8
输出：0
解释：
8 的二进制是 0b1000 。
在 8 的二进制表示中没有连续的 1，所以返回 0 。
提示：
1 <= N <= 10^9
'''
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        print(bin(N))
        n = -1
        k = []
        for i in bin(N)[2:]:# bin(N)[2:] 得到二进制2位以后的数
            if int(i) == 1 and n < 0:#当第一次出现1时
                n+=1
            elif int(i) == 1 and n >= 0:#当第二次出现1时
                n+=1
                k.append(n)
                n = 0
            else:#当不出现!时
                n+=1
        if k == []:#当没有出现第二次1时
            return 0
        return max(k)

    def binaryGap2(self, N):
        # N >> i   >>是右移，右移1位相当于除以2   0b10111   0b1011
        # &按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
        # if (N >> i) & 1 这意思是右移1位,如果移除的是1,就添加到A里
        A = [i for i in range(32) if (N >> i) & 1]
        if len(A) < 2: return 0 # 如果少于两个1,返回0
        return max(A[i + 1] - A[i] for i in range(len(A) - 1))# 用后面的数减去前面的数

    def binaryGap3(self, N):
        # 举一返三
        B = [i for i in range(len(bin(N)[2:])) if bin(N)[2:][i] == '1']
        if len(B) < 2: return 0
        return max(B[i + 1] - B[i] for i in range(len(B) - 1))

# 思路:记录下该二进制表示中每个 1 的索引。计算数组中相邻值.
print(Solution().binaryGap(N=23))
print(Solution().binaryGap2(N=23))
print(Solution().binaryGap3(N=23))