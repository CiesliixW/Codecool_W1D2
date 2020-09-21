#boolean: True False
#int: -20, 3000, 1, 2, 3, 4, 
#Float: 20.23 , 3.1415 ,
#String: "elo elo" , ' elo elo'
#List: [] - agreguje w sobie inne typy 
# funkcja type - zwraca typ 
# a+ = 10 to to samo co a = a + 10 

#import os
#os.system("cls || clear")

####################################

# import os

# os.system("cls || clear")

# user_age = input("Give your age: ")

# result_age = int(user_age) + 20

# os.system("cls || clear")

# user_name = input("Give your name: ")


# print(user_name + "Your age after 20 years will be: " + str(result_age))


########################################

# range(len(int_number)) => [0,1,2,3,4,5,6,7......20]

int_number = [1,2,3,4,10,11,12,13,12,8]
# my_sum = 0
# for number in int_number: #number przyjmuje wartści z tej listy int_number po kolei
#     print(number)

###################################

# for i in range(len(int_number)):
#     for j in range(len(int_number)):
#         print(f"i = {i}; j = {j}") 


###################################

# user_input = ""
# EXIT_WORD = "quit" 
# should_continue = True

# while should_continue:
#     user_input = input("Give a number to calculate the square:  ")
    
#     if user_input == EXIT_WORD:
#         should_continue = False
#     else:
#         square = int(user_input) * int(user_input)
#         print(f"The Square is: {square}")
#         input("Press enter to continue")

# print("end of the program")


###################################################
import os

def square():
        user_input = input("Give a number to calculate the square:  ")
        square = int(user_input) * int(user_input)
        print(f"The Square is: {square}")
        input("Press enter to continue")
        

def cube():
        user_input = input("Give a number to calculate the cube:  ")
        cube = int(user_input) * int(user_input)* int(user_input)
        print(f"The cube is: {cube}")
        input("Press enter to continue")

def sorting_function():
        number_of_numbers = input("Give a number of numbers: ")
        list_of_number = []
        for i in range(int(number_of_numbers)):
            number = input("Give a number: ")
            list_of_number.append(int(number))
        print(f"Your numbers are: {list_of_number}")
        input("press enter to contiune")

def menu():
    os.system("cls || clear")
    print("(1) - calculate square \n")
    print("(2) - calculate cube \n")
    print("(4) - sort numbers \n")
    print("quit - to end the program\n\n")

    user_option = input("choose the function by number: ")

    if user_option == EXIT_WORD:
        should_continue = False

    if user_option == "1":
        square()


    if user_option == "2":
        cube()

    if user_option == "4":
        sorting_function()
    

EXIT_WORD = "quit"

should_continue = True
while should_continue:
    menu()

