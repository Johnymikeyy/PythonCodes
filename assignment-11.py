#Is it Prime Number

number = int(input("Please enter the number you want to learn whether is Prime Number or not\n"))
primekey = 0

for i in range(2,number):
    if number % i == 0:
        print("{} is not a Prime Number.".format(number))
        primekey += 1
        break

print((not primekey) * f"{number} is a Prime Number.")