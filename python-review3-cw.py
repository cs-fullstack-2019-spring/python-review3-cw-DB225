def main():
    #problem1()
    #problem2()
    #problem3()
    #problem4()

#PROBLEM1
#Given a number n, return True if n is in the range 1..10, inclusive.
# Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
# Print the result returned from your function.
#BONUS: Get the number and outside_mode flag from User input instead of hardcoding it
#def in1to10(n, outside_mode):
#Examples of Expected Output:
#in1to10(5, False) → True
#in1to10(11, False) → False
#in1to10(11, True) → True
def problem1():
    print(in1to10(5, False))
    print(in1to10(11, False))
    print(in1to10(11, True))
def in1to10(n, outside_mode):
    userInput = int(input("Put a number: "))
    for n in range(1,11):
        if(userInput>=1 or userInput <= 10):
            return True
        else:
            return False

##################################################################################
#PROBLEM2
#Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.
#Once the user enters the equal sign to quit, print all the strings that were entered as one line with each word separated by a comma and space.
#Example of Expected Output:
#You, Entered, These, Words, Today
def problem2():
    userInput = ''
    Array = []

    while (userInput != "="):
        userInput = input("Put a string: ")
        Array.append(userInput)
    print(','.join(Array))

##################################################################################
#PROBLEM3
#Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Print the result from your function.
#BONUS: Get the number from User input instead of hardcoding it
#def near_ten(num):
#Examples of Expected Output:
#near_ten(12) → True
#near_ten(17) → False
#near_ten(19) → True
def problem3():
    userInput = int(input("Put a number: "))
    while (userInput > 0):
        if(userInput%2 == 0):
            print(f'{userInput} = True')
def near_ten(num):
    print()

##################################################################################
#PROBLEM4
#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
# Note: There isn't any restriction on how your approach determining what the min and max values are.
#def big_diff(nums):
#Examples of Expected Output:
#big_diff([10, 3, 5, 6]) → 7
#big_diff([7, 2, 10, 9]) → 8
#big_diff([2, 10, 7, 2]) → 8
def problem4():
    myArray = [12,3,4,5,64,1,2]



















##################################################################################
if __name__ == '__main__':
    main()