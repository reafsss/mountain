# Q1_팩토리얼은 단순 for문으로도 구할 수 있지만, 학습을 위해 재귀를 써 봅시다.
def factorial(num):
    if num == 0:
        return 1
    return num*factorial(num-1)

num=int(input())
print(factorial(num))