#Q9_크로아티아 알파벳의 개수를 세는 문제
word = input()
list1=['z=', 's=', 'nj', 'lj', 'd-', 'dz=', 'c-', 'c=']
list1.reverse()
for i in list1:
    word=word.replace(i, 'A')
print(len(word))