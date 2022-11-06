class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p = 0
        for i in range(len(t)):
            letter_s = s[p] if p < len(s) else ''
            if letter_s == '':
                break
            if t[i] == letter_s:
                p += 1
        return p == len(s)

s = Solution()
print(s.isSubsequence("", "abc"))