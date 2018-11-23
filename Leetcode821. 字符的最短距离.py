'''
给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。
示例 1:
输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
说明:
字符串 S 的长度范围为 [1, 10000]。
C 是一个单字符，且保证是字符串 S 里的字符。
S 和 C 中的所有字母均为小写字母。
'''
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        for i in range(len(S)):
            left , right = S[i-len(S)::-1].find(C) , S[i:].find(C)
            #S[i-len(S)::-1]向左找C   S[i:]向右找C
            # 为什么S[i-len(S)::-1]要写-1,因为方向性,-1就是向后
            # 为什么left会等于-1.因为S[i-len(S)::-1]是倒序,find(C)找到的C总是在最后一位
            if left == -1: left = 10000
            # 如果向左找到的另一头的C,那么把left变为10000,这样和right比,min(),就会选择right
            #认为10000已经足够大（字符串总长）
            if right == -1: right = 10000
            res.append(min(left , right))
        print(res)
        return res
Solution().shortestToChar(S = "loveleetcode", C = 'e')