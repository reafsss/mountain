#Q7
number = int(input())
score=[]
for i in range(number):
    score.append(list(map(int, input().split())))

for i in score:
    average=sum(i[1:])/i[0]
    count=0
    for j in i[1:]:
        if j>average:
            count+=1
    print("%0.3f%%"%(count/i[0]*100))