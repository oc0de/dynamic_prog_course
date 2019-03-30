class Knapsack(object):
    def solve_knapsack(self, profits, weights, capacity):
        return self._knapsack(profits, weights, capacity, 0)
    
    def _knapsack(self, profits, weights, capacity, currentIndex):
        if (capacity <= 0 or currentIndex >= len(profits)):
            return 0

        profit1 = 0
        if (weights[currentIndex] <= capacity):
            profit1 = profits[currentIndex] + self._knapsack(profits, weights, 
                                                capacity-weights[currentIndex], currentIndex+1)
        
        profit2 = self._knapsack(profits, weights, capacity, currentIndex+1)

        return max(profit1, profit2)


ks = Knapsack()
profits = [1,6,10,16] 
weights = [1,2,3,5]
maxProfitT1 = ks.solve_knapsack(profits, weights, 7)
maxProfitT2 = ks.solve_knapsack(profits, weights, 6)
if ( maxProfitT1 == 22 and maxProfitT2 == 17): print("Success")




