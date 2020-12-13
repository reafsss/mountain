# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.

# Test
name = "alex"
typed = "aaleex"

name == typed

name_list=list(name)
typed_list=list(typed)

temp3 = []
for i in name_list:
    if i*2 in typed_list:
        temp3.append(i)
print(temp3)

# 1. 원래 이름이랑 타이핑이랑 비교
# 2. 중복된 값 확인
# 3. 중복된 값 뺏을때 원래 이름과 같은지 확인