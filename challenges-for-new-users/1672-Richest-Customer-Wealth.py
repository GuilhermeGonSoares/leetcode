class Solution(object):
    def maximumWealth(self, accounts):
        richer = 0
        for wealth in accounts:
            if sum(wealth) > richer:
                richer = sum(wealth)
        return richer

