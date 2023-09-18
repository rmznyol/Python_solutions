# 739. Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for temp in temperatures]
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                j, _ = stack.pop()
                answer[j] = index - j
            stack.append((index,temp))
        return answer
##################################################################
# 901. Online Stock Span
class StockSpanner:

    def __init__(self):
        self.history = []
        

    def next(self, price: int) -> int:
        if not self.history:
            self.history.append([price,1])
            return 1
        if self.history[-1][0] <= price:
            self.history[-1][0] = price
            self.history[-1][1] += 1
        else:
            self.history.append([price,1])
        i = span = 0 
        l = len(self.history)
        while i < l and self.history[-1-i][0] <= price:
            span += self.history[-1-i][1]
            i += 1
        return span
