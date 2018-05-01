

# Countdown

def countdown(num):
    numArray = []
    for i in range(num, -1, -1):
        numArray.append(i)
        print(i)
    # print('There are '+ str(len(numArray)) +' items in the array')
    return numArray

arrCount = countdown(10)
print(arrCount)
# countdown(10)

# ------------------------------------------------------------------ #

# Print and Return

def printReturn(arr):
    print(arr[0])
    return arr[len(arr)-1]

returnVal = printReturn([1, 10])
print(returnVal)

# ------------------------------------------------------------------ #

# First Plus Length

def firstSum(arr):
    first = arr[0]
    sum = first + len(arr)
    return sum

print(firstSum([1, 2, 3, 4, 5]))


# ------------------------------------------------------------------ #

# Values Greater than Second

def greaterThanSecond(arr):
    newArray = []
    if len(arr) < 2:
        return False
    for i in arr:
        if i > arr[1]:
            newArray.append(i)
            print(i)
    print(len(newArray))
    return newArray

seeArray = greaterThanSecond([1, 4, 3, 4, 5])
print(seeArray)

# ------------------------------------------------------------------ #

# This Length, That Value

def thisLengthThatValue(num1, num2):
    retArray = []
    if num1 == num2:
        print('Jinx!')
    for i in range(0, num1):
        retArray.append(num2)
    return retArray

whatArray = thisLengthThatValue(5, 2)
print(whatArray)