#Q1_두수를비교한결과를출력
a,b=map(int,input().split())
if a > b:
    print(">")
elif a==b:
    print("==")
else:
    print("<")