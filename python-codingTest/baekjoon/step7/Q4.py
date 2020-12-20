#Q4_각 문자를 반복하여 출력하는 문제
number = int(input())
list1=[]
for i in range(number):
    list1.append(list(map(str, input().split())))

for i in list1:
    if len(i)==2:
        for j in i[1]:
            print(j*int(i[0]),end='')
        print("")
