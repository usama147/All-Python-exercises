x = ["apple", "orange"]
y = ["apple", "orange"]
z = x

print(x is z)
# Returns true because z is the same as x

print(x is y)
# Returns false because x is not the same as y even if they have the same contents.

print(x == y)
# To demonstrate the difference between "is" and "=="
# This comparison returns true because x is equal to y


x = ["apple", "orange"]
y = ["apple", "orange"]
z = x

print(x is not z)
# Returns false because z is not the same object as x

print(x is not y)
# Returns true because x is not the same object as y, even if they have the same content.

print(x != y)
# To demonstrate the difference between "is not" and "!=" : this comparison returns false because x is equal to y.
