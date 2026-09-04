#asking to enter the number
user_input = input('enter your word:')
#Changes the entered word to uppercase
user_input = user_input.upper()

#using for loop to processing data
for Letter in user_input:
    #checking if the letter is a vowel
    if Letter == 'A':
        continue
    if Letter == 'I':
        continue
    if Letter == 'U':
        continue
    if Letter == 'E':
        continue
    if Letter == 'O':
        continue 
    else:
        #Printing consonants
        print(Letter)



