class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        soma = 0
        result = []
        for x in nums:
            soma += x
            result.append(soma)
        return result

s = Solution()
print(s.runningSum([3,1,2,10,1]))