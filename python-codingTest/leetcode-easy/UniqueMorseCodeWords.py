# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation: 
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."

# There are 2 different transformations, "--...-." and "--...--.".

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

# Test
words = ["gin", "zen", "gig", "msg"]
grammer = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
abc = list("abcdefghigklmnopqrstuvwxyz")

dic = {abc:grammer for abc, grammer in zip(abc, grammer)}
transformed=[]
for i in words:
    word=''
    for j in i:
        word+=dic[j]
    transformed.append(word)
    

print(transformed, set(transformed))