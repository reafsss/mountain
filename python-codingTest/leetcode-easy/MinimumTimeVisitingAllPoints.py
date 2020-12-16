# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7

# Test
points = [[1,1],[3,4],[-1,0]]

list1=[1,1]
list2=[3,4]
list3=[]
for i, j in list1, list2:
    print(i, j)
    list3.append(abs(i-j))

print(list3)
# for i, j in enumerate(points):
#     time = 