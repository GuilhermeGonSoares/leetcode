class Solution(object):
    def maximum69Number (self, num):
        digits = [x for x in str(num)]
        found = False
        i = 0
        while i < len(digits) and not found:
            if digits[i] == '6':
                digits[i] = '9'
                found = True
            i += 1
        return int(''.join(digits))

s = Solution()
print(s.maximum69Number('9669'))
