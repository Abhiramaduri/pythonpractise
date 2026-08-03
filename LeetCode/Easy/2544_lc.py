class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=0
        digit=str(n)
        for i in range(len(digit)):
            a=int(digit[i])
            if i%2==0:
                sum +=a
            else:
                sum -= a
        return sum