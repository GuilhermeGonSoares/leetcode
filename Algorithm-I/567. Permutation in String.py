from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2): return False
        w, ctr, count = len(s1), Counter(s1), 0
        for j in range(len(s1)):
            if s2[j] in s1:
                ctr[s2[j]] -= 1
                if ctr[s2[j]] >= 0: count += 1
        if count == len(s1):
            return True
        for i in range(1, len(s2) - w + 1):
            eliminate = s2[i-1]
            add = s2[w+i-1]
            if eliminate in s1:
                ctr[eliminate] += 1
                if ctr[eliminate] > 0: count -= 1
            if add in s1:
                ctr[add] -= 1
                if ctr[add] >= 0: count += 1
            if count == len(s1):
                return True
        return False
                

            
s = Solution()
print(s.checkInclusion("a","ab"))

