# Python Binary Search

## This program will generate a list of 1000 ordered numbers
#Then it will generate a random number from 1 - 1000 
#it will perform a binary search and look for the random numbers in 
#the provided list of numbers from 1 - 1200

### STEP 1. 
* Setup working environment, Header Notes/README.
I used Visual Studio Code and Python as my working environnment for this project. I then created a README file in my github account to display
and showcase my steps during the project. 

### STEP 2.
* generate a list of 1000 ordered numbers since the binary search needs it to be ordered in order to search throught the list

### STEP 3.
* generate one unique single number randomly picked from 1 - 1200

### STEP 4.
* run the binary search function the randomly picked number against the list of 1000 ordered numbers and see if the number is available.

### STEP5. 
* The binary search will look at the middle element of the array of 1000 items. If the item is to big, it will eliminate the right half of the array and repeat. If it is too small, it will eliminate the left half of the array and repeat. Once the searched items is found from the sub-array size 0, the function stops and returns a result.

### Result
* If the randomly picked number is found in the list, it returns the index where the number is located, if the number is nowhere in the list, then it returns "Not found"

### Final Comments:
* The application overall was pretty straight foward. The only challenge I had was trying to figure out how to get the list ordered since I was using the random list from last project, but when I went back to basics I realized that I can simply use the orginal list from the list in range of 0,1001 so that helped me to move foward with my application.
