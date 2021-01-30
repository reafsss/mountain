# 재귀함수_2
# 별 찍기

num = int(input())

num = 9

def star(num):
    print('***')
    print('* *')
    print('***')
    return star_recursive(int(num/3))

def star_recursive(num):
    if num == 1:
        return
    return star(num)
