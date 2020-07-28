#Count the number of each letter in a sentence.

text = input("please enter the sentence you want to counts the number of each letter of\n").lower()
result = {}

for i in text:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
    
print(result)