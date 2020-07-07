#Finds out the most frequent number in the given list.
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
frequent_num = max(numbers, key = numbers.count)
print(f"The most frequent number is {frequent_num} and it was {numbers.count(frequent_num)} times repeated")