class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str'
        :rtype: bool
        """

        r = set(ransomNote)
        for letra in r:
            if ransomNote.count(letra) > magazine.count(letra):
                return False
        return True

s = Solution()
print(set("fihjjjjei"))
print(s.canConstruct("fihjjjjei", "hjibjjjagacbhadfaefdjaeaebgi"))