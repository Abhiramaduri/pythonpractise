class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def get_cost(minutes: int, seconds: int) -> int:
            if not (0 <= minutes <= 99 and 0 <= seconds <= 99):
                return float('inf')
            digits_str = str(minutes * 100 + seconds)           
            cost = 0
            curr_pos = str(startAt)
            for digit in digits_str:
                if digit != curr_pos:
                    cost += moveCost
                    curr_pos = digit
                cost += pushCost
                
            return cost
        m1 = targetSeconds // 60
        s1 = targetSeconds % 60
        m2 = m1 - 1
        s2 = s1 + 60
        return min(get_cost(m1, s1), get_cost(m2, s2))