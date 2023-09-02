# 739. Daily Temperatures


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
