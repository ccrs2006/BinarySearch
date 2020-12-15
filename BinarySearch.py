#This program will generate a list of 1000 ordered numbers
#Then it will generate a random number from 1 - 1000 
#it will perform a binary search and look for the random numbers in 
#the provided list of numbers from 1-1200

#import pythomrandom library
import random

#generate a list of ordered numbers between 0 - 1000
randomList = list(range(0,1001))
print(randomList)
#generate a unique random number in between 0 - 1200
randomNumber = random.randint(0,1201)
print(randomNumber)

#binary search function
def binarySearch(sequence, item):
    begin_index = 0
    end_index = len(sequence)-1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) //2
        midpoint_value = sequence[midpoint]

        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint -1

        else: 
            begin_index = midpoint + 1
    return ("Not found")

#Driver code
Test_Sequence = randomList
searched = randomNumber
print(Test_Sequence)
print("From a list of integers 0 to 1000 we are looking for random integer:")
print(searched)
print("After running binary search the index number for this random integer is: ")
print(binarySearch(Test_Sequence, searched))