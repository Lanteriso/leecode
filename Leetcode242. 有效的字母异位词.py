'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
示例 1:
输入: s = "anagram", t = "nagaram"
输出: true
示例 2:
输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。
进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
'''
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 思路:比较两个字符串每个字母的个数是否相等 str.count(sub) 放弃
        # 思路2: 排序字符串
        ss = sorted(list(s))
        tt = sorted(list(t))
        print(ss,tt)
        return sorted(list(s))==sorted(list(t))


if __name__ == "__main__":
    Solution().isAnagram(s = "dgncpmbgmg", t = "dgggsmmtnc")