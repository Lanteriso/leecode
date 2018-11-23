'''
我们要把给定的字符串 S 从左到右写到每一行上，每一行的最大宽度为100个单位，如果我们在写某个字母的时候会使这行超过了100 个单位，那么我们应该把这个字母写到下一行。我们给定了一个数组 widths ，这个数组 widths[0] 代表 'a' 需要的单位， widths[1] 代表 'b' 需要的单位，...， widths[25] 代表 'z' 需要的单位。
现在回答两个问题：至少多少行能放下S，以及最后一行使用的宽度是多少个单位？将你的答案作为长度为2的整数列表返回。
示例 1:
输入:
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
输出: [3, 60]
解释:
所有的字符拥有相同的占用单位10。所以书写所有的26个字母，
我们需要2个整行和占用60个单位的一行。
示例 2:
输入:
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"
输出: [2, 4]
解释:
除去字母'a'所有的字符都是相同的单位10，并且字符串 "bbbcccdddaa" 将会覆盖 9 * 10 + 2 * 4 = 98 个单位.
最后一个字母 'a' 将会被写到第二行，因为第一行只剩下2个单位了。
所以，这个答案是2行，第二行有4个单位宽度。
'''
class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        # 已知 每一行的最大宽度为100个单位 求 行数 和 最后一行的单位
        # 当 宽 >=100 时 行数 +1 所以
        # 已知 数组 widths ，这个数组 widths[0] 代表 'a' 需要的单位， widths[1] 代表 'b' 需要的单位，...，
        # widths[25] 代表 'z' 需要的单位,得到字典dict(zip(st,widths))
        st= "abcdefghijklmnopqrstuvwxyz"
        li = 1
        alli = 0
        wi = dict(zip(st,widths))
        for i in S:
            alli = alli + wi.get(i)
            if alli == 100:#当字符刚好占满一行时 行数加一 并且下一行从0开如计算
                li+=1
                alli=0
            elif alli > 100:#当字符占满超过一行时 行数加一 并且下一行从当前字符单位wi.get(i)开如计算
                li+=1
                alli = wi.get(i)
        return li,alli

    def numberOfLines1(self, widths, S):#最快的算法
        lnum = 1
        lwidth = 0
        ord_a = ord('a')# ord('a')=97   ord('b')=98  wisths[0]=ord('a')-ord('a')  wisths[1]=ord('b')-ord('a')
        for ch in S:
            width = widths[ord(ch)-ord_a]
            lwidth += width
            if lwidth > 100:
                lnum += 1
                lwidth = width
        return [lnum, lwidth]

print(Solution().numberOfLines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
S = "bbbcccdddaaa"))
print(Solution().numberOfLines1(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
S = "bbbcccdddaaa"))