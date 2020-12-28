# Test
groupSizes = [3,3,3,3,3,1,3] #Input
group_num = list(set(groupSizes))
group_num.sort()
list2=[]
for i in group_num:
    line=[]
    n=i
    for j,k in enumerate(groupSizes):
        if i == k:
            line.append(j)
    result = [line[l * n:(l + 1) * n] for l in range((len(line) + n - 1) // n )] 
    for m in result:
        list2.append(m)
print(list2) #Output

# class Solution:
#     def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
#         group_num = list(set(groupSizes))
#         group_num.sort()
#         list2=[]
#         for i in group_num:
#             line=[]
#             n=i
#             for j,k in enumerate(groupSizes):
#                 if i == k:
#                     line.append(j)
#             result = [line[l * n:(l + 1) * n] for l in range((len(line) + n - 1) // n )] 
#             for m in result:
#                 list2.append(m)
#         return list2

# def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
#         sizeToGroup, res = collections.defaultdict(list), []
#         for i, size in enumerate(groupSizes):
#             sizeToGroup[size].append(i)
#             if len(sizeToGroup[size]) == size:
#                 res.append(sizeToGroup.pop(size))
#         return res