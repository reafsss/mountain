# Q1_기본출력
print("Hello World!")

# Q2_반복출력
for i in range(0,2):
    print("강한친구 대한육군")

# Q3_특수문자출력1
print("\    /\\\n\
 )  ( ')\n\
(  /  )\n\
 \(__)|")

# Q4_특수문자출력2
print("|\_/|\n\
|q p|   /}\n\
( 0 )\"\"\"\\\n\
|\"^\"`    |\n\
||_/=\\\__|")

# Q5_두수를입력받고합을출력
a, b = map(int, input().split())
print(a+b)

# Q6_두수를입력받고뺄셈을한결과를출력
a, b = map(int, input().split())
print(a-b)

# Q7_두수를입력받고곱을출력
a, b=map(int, input().split())
print(a*b)

# Q8_두수를입력받고나눗셈을한결과를출력
a,b = map(int, input().split())
print(a/b)

# Q9_두수를입력받고A+B,A-B,A*B,A/B(몫),A%B(나머지)를출력
a,b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

# Q10_나머지연산
A,B,C=map(int,input().split())
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

# Q11_(세 자리 수)×(세 자리 수)중두번째연산출력
a,b = [str(input()) for _ in range(2)]
for i in b[::-1]:
    print(int(a)*int(i))
print(int(a)*int(b))

a,b = [str(input()) for _ in range(2)] #runtime줄이기
print(int(a)*int(0))#runtime줄이기
print(int(a)*int(1))#runtime줄이기
print(int(a)*int(2))#runtime줄이기
print(int(a)*int(b))#runtime줄이기