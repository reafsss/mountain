# Test
accounts = [[1,5],[7,3],[3,5]] #Input
customerList=[]
for i in range(len(accounts)):
    summ = 0
    for j in range(len(accounts[i])):
        summ += accounts[i][j]
    customerList.append(summ)
print(max(customerList)) #Output

# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         customerList=[]
#         for i in range(len(accounts)):
#             summ = 0
#             for j in range(len(accounts[i])):
#                 summ += accounts[i][j]
#             customerList.append(summ)
#         return max(customerList)

# Problem Analysis
# 1. sum each account
# 2. return Max value 

# customer1 = accounts[0][0] + accounts[0][1]
# customer2 = accounts[1][0] + accounts[1][1]
# customer3 = accounts[2][0] + accounts[2][1]