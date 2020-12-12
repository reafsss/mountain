accounts = [[1,5],[7,3],[3,5]]

customer1 = accounts[0][0] + accounts[0][1]
customer2 = accounts[1][0] + accounts[1][1]
customer3 = accounts[2][0] + accounts[2][1]

if customer1 > customer2:
    wealthCustomer = customer1
elif customer2 > customer3:
    wealthCustomer = customer2
else :
    wealthCustomer = customer3

print(wealthCustomer)