#Print the prime numbers which are between 1 to entered limit number (n).

n = int(input("please enter the a number which you want\
 to find prime number between 1 to\n"))

number = []

for i in range(1,n+1):
    count = 0
    for j in range(2,i):
        if i % j ==0:
            count +=1
    if count == 0:
        number.append(i)

print(number)
