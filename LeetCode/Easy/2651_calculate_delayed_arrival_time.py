class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        ans = (arrivalTime + delayedTime)%24
        return(ans)