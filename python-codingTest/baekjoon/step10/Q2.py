# Q2_n번째 피보나치 수를 구하는 프로그램
n=int(input())
n=10

def Fibonacci(a):
    if a <= 1:
        return a
    elif a==2:
        return 1
    return Fibonacci(a-1)+Fibonacci(a-2)

Fibonacci(10)