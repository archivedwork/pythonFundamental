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

