maxnum=21
alist=[5,6,7,8,9]
blist=[]
summ=0
for i,a in enumerate(alist):
    for j,b in enumerate(alist[i+1:]):
        blist=alist[i+1:]
        for k,c in enumerate(blist[j+1:]):
            summ = a + b + c
            blist.append(summ)
            # print()
# print(max(blist))
blist
