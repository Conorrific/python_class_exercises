def spam():
    """simple 'Hello World!' function"""
    print("Hello World!")
spam()
def square(n):
    """returns the square of a number."""
    squared = n ** 2
    print( "%d squared is %d. " % (n, squared))
    return squared
square(19)

"""When defining a function, placeholder variables
are called parameters. 

When using, or calling, a 
function, inputs into the function are called arguments"""

def power(base, exponent):
    result = base ** exponent
    print("%d to the power of %d is %d." % (base, exponent, result))

power(37, 4)

""" a function can call another function"""

def function_one(n):
    return n * 5

def function_two(m):
    return function_one(m) + 7
#new fucntion 
def cube(number):
    return number * number * number
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else: return False
print(by_three(9))

def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

print(shut_down("yes"))
