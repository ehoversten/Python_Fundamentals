def a():
    return 5
print(a())

# >> 5
#   ------------------

def a():
    return 5
print(a()+a())

# >> 10
#  ------------------

def a():
    return 5
    return 10
print(a())

# >> 5
#  ------------------

def a():
    return 5
    print(10)
print(a())


# >> 5
#   ------------------

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a)


# >> 100
#  5
# ------------------


def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# >> 7
# >> 14
# >> 21
#  ------------------

def a(b,c):
    return b+c
    return 10
print(a(3,5))

# >> 8
#  ------------------

b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# >> 500
#  300
#  500
#  300
#  500
# ------------------

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# >> 500
#  300
#  300
#  500
#  300
#  300
#  500
#  ------------------

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

# >> 500
#   500
#   300
#   300

