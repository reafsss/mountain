# Test
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
prices= [7,6,4,3,1]

profit_max=[]
for i in range(len(prices)):
    buy=prices[i]
    profit=[]
    for j in prices[i+1:]:
        profit.append(j-buy)
    if profit==[]:
        break
    profit_max.append(max(profit))

if profit_max == []:
    profit_max.append(0)
elif max(profit_max) <0:
    profit_max.append(0)

max(profit_max)