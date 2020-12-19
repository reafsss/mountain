#Q3
a = int(input())
b = int(input())
c = int(input())

k = a*b*c
k_list = list(str(k))
for i in range(10):
    k_num_count = k_list.count(str(i))
    print(k_num_count)

# runtime error가 뜸

# num_list = []
# for i in range(3):
#     num_list.append(int(input()))
# product=1
# for i in num_list:
#     product=product*i
# for i in range(0,10):
#     count=0
#     for j in product:
#         if int(j)==i: count+=1
#     print(count)