#Q5_주어진 단어에서 가장 많이 사용된 알파벳을 출력하는 문제
word=input().upper()
t=[]
word_dedupli = list(set(word))
for i in word_dedupli:
    t.append(word.count(i))

idx=[i for i, x in enumerate(t) if x==max(t)]
if len(idx)>1: print('?')
else : print(word_dedupli[t.index(max(t))])


# 시간초과1
# word = input().upper()
# dic={}
# for i in word:
#     count=0
#     for j in word:
#         if i == j:
#             count+=1
#     dic[i]=count
# dic_values=list(dic.values())
# dic_max=max(dic.values())
# dic_count=dic_values.count(dic_max)
# if dic_count==1:
#     for i, j in dic.items():
#         if j == dic_max:
#             print(i)
#             break
# else :
#     print('?')

# 시간초과2
# word = input().upper()
# list1=[]
# for i in word:
#     list1.append(i)
#     count=0
#     for j in word:
#         if i == j:
#             count+=1
#     list1.append(count)
# list1_values=list(set(list1[1::2]))
# list1_max=max(list1_values)
# list1_count=list1_values.count(list1_max)
# if list1_count==1:
#     for i in list1:
#         if i == list1_max:
#             print(list1[list1.index(i)-1])
#             break
# else :
#     print('?')