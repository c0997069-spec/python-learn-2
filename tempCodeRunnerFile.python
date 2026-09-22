#Bank Database
User_Name = ['Harry142', 'Karl712', 'Alex872', 'Shin6252', 'Akiha625', 'Yosh629']
Pin = ['123872', '726362', '889173', '612637', '726514', '981630']

#Trial Test
Trial = 0

print('=======WELCOME TO BANK OF CERYDRA=======')

#Process
while Trial < 3:  
    Input_User_Name = input('Please Enter Your User Name: ')
    
    if Input_User_Name in User_Name:
        index = User_Name.index(Input_User_Name)
        Input_Pin = input('Please Enter Your Pin in Here: ') 
        
        if Input_Pin == Pin[index]:
            print(f"Welcome {User_Name[index]}! You have successfully logged in.")
            break  # Keluar loop jika login berhasil
        else:
            print("PIN Incorrect!")
    else:
        print("Username Didnt Found!")
        
    Trial += 1  
    print(f"remaining attempts: {3 - Trial}\n")

if Trial == 3:
    print("Trial expired! Account blocked..")
