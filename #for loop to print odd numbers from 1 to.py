#for loop to print odd numbers from 1 to 10

for i in range (1,11):
    if i % 2 == 1:
        print(i)


#while loop that counts from 0 to 10, and prints odd numbers to the screen.

x = 0
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

#create program with continue and break

for ch in "alex.yanto@Wmail.com":
    if ch == "@":
        break
    if ch == ".":
        continue
    print(ch)

# Create a program with a for loop and a continue statement.

for digit in "0123456789":
    if digit == "0":
        print('x', end='')
    continue
print(digit, end='')

# exaple from while loop
n = 3
 
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

#example of for loop
n = range(3)
 
for num in n:
    print(num - 1)
else:
    print(num)

for B in range(0, 2, 4):
    print(B)



