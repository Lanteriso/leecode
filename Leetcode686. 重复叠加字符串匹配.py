''' 给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。

举个例子，A = "abcd"，B = "cdabcdab"。

答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。

注意:

 A 与 B 字符串的长度在1和10000区间范围内。'''

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        i = 1
        while len(B)<=10000 and len(A*i)<=10000:
            if B in A*i:
                return i
            i += 1
        return -1

    def repeatedStringMatch2(self, A: str, B: str) -> int:
        if len(set(A)) < len(set(B)):
            return -1
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q + i):
                return q + i
        return -1


if __name__ == '__main__':
    print(Solution().repeatedStringMatch(A="aa", B="a"))
    print(Solution().repeatedStringMatch2(A="aa", B="a"))
