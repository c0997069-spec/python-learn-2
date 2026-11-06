#Powered List ⚡
#Coppying some part of the list
list_1 = [10,9,8,7,6,5]
New_list = list_1[1:4]
print(New_list)

#Coppying all part of the list
List_2 =[1,2,3,4,5,6]
New_list_2 = List_2[:]
print(New_list_2)

#Slices negative index
my_list_3 = [1,3,4,5,6,7,9,10]
new_list_3 = my_list_3[3:-1]
print(new_list_3)

#Del instruction
my_list_4 = [2,3,4,5,7,8,9,10,25]
del my_list_4[3:5]
print(my_list_4)

#in and not in operator
my_list_5 = [0,2,7,1,9]
print(4 in my_list_5)
print(6 in my_list_5)
print(9 in my_list_5)

#program example
my_list_storage = [22,5,15,8,9,10,7,1,3,2]
largest = my_list_storage[0]
for i in range(5, len(my_list_storage)):
    if my_list_storage[i] > largest:
        largest = my_list_storage[i]
print(largest)

