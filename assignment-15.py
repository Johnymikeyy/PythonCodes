#Print the FizzBuzz numbers.

number = []

for i in range(1,100):
    print("{}".format("FizzBuzz" if i % 3 == 0 and i % 5 == 0 \
        else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i),\
            end=",")
