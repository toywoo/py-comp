numbers = [9, 6, 7, 1, 8, 4, 5, 3, 2]


print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

new_list1 = sorted(numbers)
print(new_list1)

new_list2 = sorted(numbers, reverse=True)
print(new_list2)