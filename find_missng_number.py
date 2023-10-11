'''
This code is for finding the missing value. 
it is valuable for the leetcode challenge interview

Given an array containing a range of numbers from 0 to n with a missing number, 
find the missing number in the input array.

------------------------------------------------------------------------
| To find the missing number in an array, we need to iterate over the   |
| input array and store the numbers in another array that we didn’t find| 
| in the input array while iterating over it. Below is how you can find |
| the missing number in an array or a list using the Python programming |
| language:                                                             |
|_______________________________________________________________________|


'''

def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output
    
listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(findMissingNumbers(listOfNumbers))