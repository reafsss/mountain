# Input: s = "RLLLLRRRLR"
# Output: 3

# Test
s = "RLRRRLLRLL"
check1=s.split('RL')
check2=s.split('LR')
print(len(check1), len(check2))



# 1. 첫번재 letter 확인
# 2. 반복수 확인
# 3. 그반복수만큼 +
# 4. 두번째 letter 확인
# 5. 반복수 확인
# 6. 그반복수만큼 +