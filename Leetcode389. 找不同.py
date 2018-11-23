'''
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。
示例:
输入：
s = "abcd"
t = "abcde"
输出：
e
解释：
'e' 是那个被添加的字母。
'''
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ns = list(s)
        nt = list(t)
        for i in range(len(ns)):
            if s[i] in t:
                nt.remove(s[i])
        return nt[0]#一个个移除t中的s

    def findTheDifference2(self, s, t):
        r = list(set(t))#去重
        for i in r:
            if s.count(i) != t.count(i):# 返回元素出现的次数不相等的元素,
                return i


if __name__ == "__main__":
    Solution().findTheDifference(s = "abcd",t = "abcde")
    Solution().findTheDifference2(s="abcd", t="abcde")
