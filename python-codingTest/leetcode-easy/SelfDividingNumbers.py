# Test
left, right = 1,222 #Input
output = []
for i in range(left,right+1):
    a=len(str(i))
    if a ==1:
        output.append(i)
    elif a==2:
        b=i%10
        c=i//10
        if b != 0 and c != 0:
            if i%b==0 and i%c==0:
                output.append(i)
    elif a==3:
        b=i%10
        c=(i%100)//10
        d=i//100
        if b != 0 and c != 0 and d != 0:
            if i%b ==0 and i%c == 0 and i%d == 0:
                output.append(i)
    elif a==4:
        b=i%10
        c=(i%100)//10
        d=(i%1000)//100
        e=i//1000
        if b != 0 and c != 0 and d != 0 and e !=0:
            if i%b ==0 and i%c == 0 and i%d == 0 and i%e == 0:
                output.append(i)        
    elif a==5:
        b=i%10
        c=(i%100)//10
        d=(i%1000)//100
        e=(i%10000)//1000
        f=i//10000
        if b != 0 and c != 0 and d != 0 and e !=0 and f != 0:
            if i%b ==0 and i%c == 0 and i%d == 0 and i%e == 0 and i%f == 0:
                output.append(i)  
print(output) #Output

# class Solution:
#     def selfDividingNumbers(self, left: int, right: int) -> List[int]:
#         output = []
#         for i in range(left,right+1):
#             a=len(str(i))
#             if a ==1:
#                 output.append(i)
#             elif a==2:
#                 b=i%10
#                 c=i//10
#                 if b != 0 and c != 0:
#                     if i%b==0 and i%c==0:
#                         output.append(i)
#             elif a==3:
#                 b=i%10
#                 c=(i%100)//10
#                 d=i//100
#                 if b != 0 and c != 0 and d != 0:
#                     if i%b ==0 and i%c == 0 and i%d == 0:
#                         output.append(i)
#             elif a==4:
#                 b=i%10
#                 c=(i%100)//10
#                 d=(i%1000)//100
#                 e=i//1000
#                 if b != 0 and c != 0 and d != 0 and e !=0:
#                     if i%b ==0 and i%c == 0 and i%d == 0 and i%e == 0:
#                         output.append(i)        
#             elif a==5:
#                 b=i%10
#                 c=(i%100)//10
#                 d=(i%1000)//100
#                 e=(i%10000)//1000
#                 f=i//10000
#                 if b != 0 and c != 0 and d != 0 and e !=0 and f != 0:
#                     if i%b ==0 and i%c == 0 and i%d == 0 and i%e == 0 and i%f == 0:
#                         output.append(i)  
#         return output