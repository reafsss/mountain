# Test
paths = [["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]] #Input
paths = [["B","C"],["D","B"],["C","A"]] #Input
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]] #Input
def destination(abc):
    return abc[1]
def start(abc):
    return abc[0]
first=[]
end = []
for i in paths:
    first.append(start(i))
    end.append(destination(i))
anwser = list(set(end)-set(first))
print(anwser[0]) #Output

# class Solution:
#     def destCity(self, paths: List[List[str]]) -> str:
#         def destination(abc):
#             return abc[1]
#         def start(abc):
#             return abc[0]
#         first=[]
#         end = []
#         for i in paths:
#             first.append(start(i))
#             end.append(destination(i))
#         anwser = list(set(end)-set(first))
#         return anwser[0]