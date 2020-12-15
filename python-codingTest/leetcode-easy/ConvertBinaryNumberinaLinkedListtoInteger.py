# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         num = ''
#         count = 1 
#         try :
#             while count > 0:
#                 num=num+str(head.val)
#                 head=head.next
#         except:
#             base = 2
#             answer = 0
#             for idx, i in enumerate(num[::-1]):
#                 answer += int(i) * ( base ** idx )
#         return answer

# Applied concept
# 1. n decimal number -> decimal number
# num = '10101'
# base = n
# answer = 0
# for idx, i in enumerate(num[::-1]):
#     answer += int(i) * ( base ** idx )