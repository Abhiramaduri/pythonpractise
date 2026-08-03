class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        total=0
        week=1
        while n>0:
            amount=week
            for _ in range(7):
                if n==0:
                    break
                total +=amount
                amount +=1
                n=n-1
            week = week+1
        return total