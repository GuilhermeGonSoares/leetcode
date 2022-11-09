class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = set(s)
        size_par = 0
        size_impar = 0
        for letter in letters:
            qtd = s.count(letter)
            if qtd % 2 == 0:
                size_par += qtd
            else:
                size_par += (qtd-1)
                size_impar += 1
        size = 1 if size_impar > 0 else 0
        size += size_par
        return size
s = Solution()
print(s.longestPalindrome("aaaadAAbbbbbcc"))
