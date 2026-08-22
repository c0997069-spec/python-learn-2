#Data base of desk
desk_numbers = [21, 55, 76, 81, 22, 101, 105]

#read to numbers
num1 =int(input('Enter your Id: '))
num2 =int(input('enter your Password:'))

#make condition
if num1 == 2543 and num2 == 1678:
    print('welcome member')
elif num1 == 2543 and num2 != 1678:
    print('Password is incorrect')
else:
    print('You are not a member')

#verification!
print('Now where is your desk?')
verification = int(input('Enter Your Desk Number:....'))

#make condition
if verification in desk_numbers:
    print(f'Your desk is in room {verification}')
else:
    print('Desk not found, you are robber!')