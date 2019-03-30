class Knapsack(object):
    def solve_knapsack(self, profits, weights, capacity):
        if (capacity <= 0): return 0
        
        dp, n = {}, len(profits)
        for i in range(n):
            dp[(i,0)] = 0
        
        for c in range(capacity+1):
            if weights[0] <= c:
                dp[(0,c)] = profits[0]

        for i in range(1, n):
            for c in range(1, capacity+1):
                profit1, profit2 = 0, 0
                if weights[i] <= c:
                    profit1 = profits[i] + dp[(i-1,c-weights[i])]
                
                profit2 = dp[(i-1,c)]
                dp[(i,c)] = max(profit1, profit2)

        return dp[(n-1,capacity)]


ks = Knapsack()
profits = [1,6,10,16] 
weights = [1,2,3,5]
maxProfitT1 = ks.solve_knapsack(profits, weights, 7)
maxProfitT2 = ks.solve_knapsack(profits, weights, 6)
if ( maxProfitT1 == 22 and maxProfitT2 == 17): print("Success bottomUp")





        
