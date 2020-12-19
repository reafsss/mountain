#Q4
n=[]
for i in range(10):
    n.append(int(input()))

values=[]
for i in n:
    values.append(i%42)

count=set(values)
print(len(count))