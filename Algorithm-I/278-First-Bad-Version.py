def isBadVersion(version) -> bool:
    if version == 4:
        return True
    return False

class Solution(object):
    def firstBadVersion(self, n):
        start = 0
        end = n
        while start <= end:
            middle = (start + end) // 2
            #[1, 2, 3, 4, 5]
            #isBadVersion(middle) -> false então o problema está para valores maiores que middle
            #isBadVersion(middle) -> true então o problema está para valores menores que middle
            if isBadVersion(middle):
                end = middle - 1
            
            elif not isBadVersion(middle):
                start = middle + 1  
        return start       
s = Solution()
print(s.firstBadVersion(5))