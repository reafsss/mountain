#Q6
# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX
number=int(input())
ox=[]
for i in range(number):
    ox.append(input())

for i in ox:
    new=i.split('X')
    summ=0
    for i in new:
        summ+=sum(list(range(1,len(i)+1)))
    print(summ)
