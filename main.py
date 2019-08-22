spam_amount = 0
spam_amount = spam_amount + 4

# this is comment line
if spam_amount > 0:
    print("But I don't want any spam")

# The * operator can be used to multiply two numbers (3 * 3 evaluates to 9), but amusingly enough,
# we can also multiply a string by a number, to get a version that's been repeated that many times.
viking_song = "Spam " * spam_amount
print(viking_song)



#Defining function
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
        among a, b and c.

        >>> least_difference(1, 5, -5)
        4
        """

    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


print(
    least_difference(1, 10, 100)
)

help(least_difference)


def greet(who="colin"):
    print("Hallo, ", who)

greet()

def mod_5(x):
    return x % 5

#By default, max returns the largest of its arguments.
# But if we pass in a function using the optional key argument,
# it returns the argument x that maximizes key(x) (aka the 'argmax').
print(max(100, 51, 14,  key=mod_5))


#Lists
primes = [2, 3, 5, 7]
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupitor"]
hands = [
    ['J', 'K', 'L'],
    ['M', 'N', 'O']
    ]

print("primes = " , primes)
print("Plants = ", planets)

#Slicing
# Take only three first elements
planets[0:3]
planets[:3]

# list elements after third element
print(planets[3:])

# all the planets except 1st and last
print(planets[1:-1])

# the last three planets
print(planets[-3:])

# changing lists
# let's say we want to rename Mars to Malacandra
planets[3] = 'Malacandra'
print(planets)

# length of a list
print(len(planets))

# sorted, returns a sorted version od list
print(sorted(planets))

#sum, give summation of numbers
print(sum(primes))

# List methods
primes.append(9) # add element to end of the list
print(primes)

# remove last element
primes.pop()
print(primes)

# searching list
print(primes.index(3))

print(3 in primes)
print('Earth' in planets)

#help(planets)



# Tuples
# Tuples is exactly the same as lists but
# 1. the syntax for creating them is () not []
t = (1, 2, 3)

# 2. they can not modify (they are immutable)
# t[1] = 100


# swapping two variables in python
a = 1
b = 0
a, b = b, a
print(a,b)


