thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# elements of tuple are unchangeable

print(len(thistuple))

#comma is required to create single element tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

thistuple = tuple(("apple", False, 33)) # note the double round-brackets
print(thistuple)
print(type(thistuple))
