class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            length = len(temperatures)
            ans = [0] * length
            stk = [] 

            for i in range( length):
                    while  stk and temperatures[i] > temperatures[stk[-1]]:
                            prev_day =    stk.pop()
                            ans[prev_day] = i - prev_day

                    stk.append(i)

            return ans
        