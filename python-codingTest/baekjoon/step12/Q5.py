# Q5
# 내림차순 정렬

num=input() #input

num_list=list(num)
num_list.sort(reverse=True)

anw=''
for i in num_list:
    anw += i

print(int(anw)) #output