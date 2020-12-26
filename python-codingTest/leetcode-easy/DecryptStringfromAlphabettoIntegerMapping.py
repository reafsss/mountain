# Test
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
s = "10#11#12"

number = list(range(1,27))
for i,j in enumerate(number):
    number[i]=str(j)
    if int(j)>9:
        number[i]=str(j)+'#'
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

rule = dict(zip(number, alphabet))

new=''
for i in number[9:]:
    if i in s:
        new+=rule[i]
new
    
s.split('#')
s = "1326#"
s.split('#')
