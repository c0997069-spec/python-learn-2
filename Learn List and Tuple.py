print('List and tupple learn')

#printing contents

numbers = [1,2,3,4,5]
print('orginals list contents:', numbers)

#printing previous list contents

numbers[0] = 111
print('\nprevious list contents:', numbers)

#coppying value and replace
numbers[1] = numbers[4]
print('add new variable:', numbers)

#deleting numbers
del numbers[1]
print(len(numbers))
print(numbers)

