# def gimmeList(aList):
#     for i in aList:
#         // returns the VALUES from the aList
#         print(i)
#         # print(aList[i])   // does NOT work
#
#     for i in range(len(aList)):
#         // returns the INDEX of the aList
#         # print(i)
#         // returns the VALUE of the aList
#         # print(aList[i])
#
# gimmeList([5, 6, 7, 8, 9, 10])
#


# Biggie Size
def makeItBig(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = 'big'
    return arr
#
biggedArray = makeItBig([-1, 3, 4, -5])
print(biggedArray)


# ------------------------------------------------------------------ #


# Count Positives
def countPositive(arr):
    count = 0
    for i in arr:
        if i > 0:
            count += 1
    arr.pop()
    arr.append(count)
    return arr

numPos = countPositive([-1, 1, 1, 1, 1])
print(numPos)

# ------------------------------------------------------------------ #

# Sum Total
def sumTotal(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

whoseTotal = sumTotal([1, 2, 3, 4])
print(whoseTotal)

# ------------------------------------------------------------------ #

# Average
def avg(arr):
    sum = 0
    for i in arr:
        sum += i
    avg = sum/len(arr)
    return avg

gimmeAvg = avg([1, 2, 3, 4])
print(gimmeAvg)

# ------------------------------------------------------------------ #

# Length
def length(arr):
    return len(arr)

arrayLength = length([1, 2, 3, 4])
print(arrayLength)


# ------------------------------------------------------------------ #

# Minimum
def min(arr):
    min = arr[0]
    if len(arr) < 1:
        return False
    for i in arr:
        if min > i:
            min = i
    return min

findMin = min([-1, -2, -3])
# findMin = min([3, 4, 3, 5, 1])
print(findMin)


# ------------------------------------------------------------------ #

# Maximum
def max(arr):
    max = arr[0]
    if len(arr) < 1:
        return False
    for i in arr:
        if max < i:
            max = i
    return max

findMax = max([1, 2, 3, 4])
# findMax = max([-1, -2, -3])
print(findMax)


# ------------------------------------------------------------------ #

# UltimateAnalyze
def analyze(arr):
    newDict = {}
    sumTotal = 0
    newDict['sumTotal'] = 0
    newDict['avg'] = 0

    newDict['min'] = arr[0]
    newDict['max'] = arr[0]
    for i in arr:
        if i > newDict['max']:
            newDict['max'] = i
        if i < newDict['min']:
            newDict['min'] = i
        newDict['sumTotal'] += i
        newDict['avg'] = newDict['sumTotal']/len(arr)
    return newDict

newAnalysis = analyze([1, 2, 3, 4, 5])
print(newAnalysis)


# ------------------------------------------------------------------ #

# ReverseList
def reverseList(arr):
    for i in range(0, int(len(arr)/2)):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr

reveredArray = reverseList([1, 2, 3, 4, 5])
print(reveredArray)