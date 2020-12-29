# Q6
# H, W, N = 호텔의 층 수, 각 층의 방 수, 몇 번째 손님 
T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    if N%H == 0 :
        th = N//H
        floor = H
    else :
        th = N//H + 1
        floor = N%H
    room=floor*100 + th
    print(room)