class Solution(object):
    def makeGood(self, s):
        #s = "abBAcC"
        i = 0
        letters = list(s)
        while i <= len(letters) - 2 and len(letters) > 0:
            if letters[i].lower() == letters[i+1].lower():
                if (not letters[i].isupper() and letters[i+1].isupper()) or (letters[i].isupper() and not letters[i+1].isupper()):
                    letters.pop(i+1)
                    letters.pop(i)
                    if i > 0: i -= 1
                else:   
                    i += 1
            else:   
                i += 1         
        return ''.join(letters)

