class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = set('aeiouAEIOU')
        start = 0
        end = len(s) - 1
        s = list(s)
        while start <= end:
            while start < end and s[start] not in vowel:
                start += 1  
            while start < end and s[end] not in vowel:    
                end -= 1
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        
        return ''.join(s)

s = Solution()
print(s.reverseVowels("leetcode"))

