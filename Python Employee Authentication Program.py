print(
   '''
O================================O
|  welcome to our Game company   |
O================================O
'''
)
Employee_Data_Based = ['Adrian', 'Alex', 'Sarah', 'John', 'Emily', 'Michael', 'Jessica', 'David', 'Sophia', 'Daniel']
Employee_Id = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
Employee_Password = ['adrian123', 'alex456', 'sarah789', 'john321', 'emily654', 'michael987', 'jessica111', 'david222', 'sophia333', 'daniel444']

Input_Role = input("Are you employee or Customer? (Enter 'Employee' or 'Customer'): ").strip().lower()
if Input_Role == 'employee':
    Input_Employee_Id = int(input("Enter your Employee ID: "))
    Input_Employee_Password = input("Enter your Password: ")

    if Input_Employee_Id in Employee_Id:
        index = Employee_Id.index(Input_Employee_Id)
        if Input_Employee_Password == Employee_Password[index]:
            print(f"Welcome {Employee_Data_Based[index]}! You have successfully logged in as an employee.")
        else:
            print("Incorrect password. Access denied.")
    else:
        print("Employee ID not found. Access denied.")

if Input_Role == 'customer':
    print('Welcome to our game company! Please explore our games and services in the showcase section.')

