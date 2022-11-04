from operator import itemgetter


class Solution(object):

    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        l = []
        for i in range(len(mat)):
            soldiers = mat[i].count(1)
            l.append((i, soldiers))
        l.sort(key=itemgetter(1))
        result = []
        for j in range(k):
            result.append(l[j][0])
        return result




s = Solution()
