class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length = 0

        start = 0
        end = 0
        current_str = ''

        while end < len(s):
            current_str += s[end]
            end += 1
            max_length = max(max_length, end - start)
            if end == len(s): return max_length
            while start < end and s[end] in current_str:
                start += 1
                current_str = current_str[1:]
                
        return max_length

s = Solution()
print(s.lengthOfLongestSubstring("GEEKSFORGEEKS"))
        