#Fibonacci Numbers

fibonacci = list()

for i in range(1,55):
    if i == 1:
        fibonacci.append(i)
        fibonacci.append(i)
    else:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    if fibonacci[i] >= 55:
        break

print(fibonacci)
