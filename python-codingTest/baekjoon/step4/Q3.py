#Q3_원래 수로 돌아올 때까지 연산을 반복하는 문제
#0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 
#먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 
#그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
a=int(input())
check=a
b=0
count=0
while True:
    b = a//10 + a%10
    a = (a%10)*10 + b%10
    count+=1
    if check==a:
        break
print(count)