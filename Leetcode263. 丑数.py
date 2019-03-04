'''
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:

输入: 6
输出: true
解释: 6 = 2 × 3
示例 2:

输入: 8
输出: true
解释: 8 = 2 × 2 × 2
示例 3:

输入: 14
输出: false
解释: 14 不是丑数，因为它包含了另外一个质因数 7。

首先除2，直到不能整除为止，然后除5到不能整除为止，然后除3直到不能整除为止。最终判断剩余的数字是否为1，如果是1则为丑数，否则不是丑数。
'''
class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        while num>1:
            if num%2 ==0 or num%3 ==0 or num%5 ==0:
                if num%2 ==0:
                    num = num / 2
                if num%5 ==0:
                    num = num / 5
                if num%3 ==0:
                    num = num / 3
            else :
                return False
        if num ==1:
            return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().isUgly(num=-2147483648))