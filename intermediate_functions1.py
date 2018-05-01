
import random


# create a function randInt() where randInt() returns a random integer between 0 to 100

def randInt():
   return int(random.random()*100)

randomNum = randInt()
print(randomNum)


# Create a function randInt(max=50) returns a random integer between 0 to 50

def randInt(max=50):
    return int(random.random()*max)

randomNum = randInt()
print(randomNum)

# Create a function randInt(min=50) returns a random integer between 50 to 100

def randInt(min=50):
    return int(random.random()*50)+min

randNum = randInt()
print(randNum)

# Create a function randInt(min=50, max=500) returns a random integer between 50 and 500

def randInt(min=50, max=500):
    return int(random.random()*max)+int(random.random()*min)

randNum = randInt()
print(randNum)

