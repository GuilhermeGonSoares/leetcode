class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        passos = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
            passos += 1
        return passos

s = Solution()
print(s.numberOfSteps(8))
        