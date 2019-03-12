'''
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果
，就返回 true ；否则返回 false 。

示例 1：

输入： A = "ab", B = "ba"
输出： true


提示：

0 <= A.length <= 20000
0 <= B.length <= 20000
A 和 B 仅由小写字母构成。
'''


class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        aa,bb=[],[]
        if len(A)>=2 and len(B)>=2:

            for i in range(len(A)):
                if A==B and A.count(A[i])>=2:
                    return True

                elif A[i] != B[i]:
                    aa.append(A[i])
                    bb.append(B[i])
            bb.reverse()
        print(aa,bb)
        return aa==bb and len(aa)>=2 and len(bb)>=2

if __name__=="__main__":
    print(Solution().buddyStrings(A = "", B = "ab"))

