# Learn About adding elements to list

#practice 1
numbers = [5,6,9,10,2,3]
print(len(numbers))
print(numbers)

numbers.append(4)
print(len(numbers))
print(numbers)

numbers.insert(1,13)
print(len(numbers))
print(numbers)

#practice 2

my_list = []

for i in range(5):
    my_list.append(i+2)

print(my_list)

#practice 3
my_variable = [8, 9, 10, 22, 1]
total = 0

for a in range(len(my_variable)):
    total += my_variable[a]

print(total)


