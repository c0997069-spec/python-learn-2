secret_number = 996

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
print(hint := 'Psst the secret number is 3 digit number with two early is same  and last digit is after five')
User_input = int(input('Enter your number here!:'))
if User_input != secret_number:
    print('Ha ha ha! You are stuck in my loop forever!')
    while User_input != secret_number:
        User_input = int(input('Enter your number here fool!:'))
if User_input == secret_number:
    print('well done mugle! your are free now XD')


