'''
给定一个矩阵 A， 返回 A 的转置矩阵。
矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
示例 1：
输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
示例 2：
输入：[[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]
'''


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B=[]
        C=[]
        for i in range(len(A[0])):
            for j in range(len(A)):
                B.append(A[j][i])
            C.append(B)
            B = []
        print(C)

    def transpose1(self, A):
        A[:] = map(list,zip(*A))
        print(A)
        return A



Solution().transpose(A=[[1,2,3],[4,5,6]])
Solution().transpose1(A=[[1,2,3],[4,5,6]])