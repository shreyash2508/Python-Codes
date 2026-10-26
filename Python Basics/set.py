# Create a set with initial values
fruits = {"apple", "banana", "cherry"}

# Create an empty set (Note: {} creates an empty dictionary!)
empty_set = set()

# Adding elements
fruits.add("orange")       # Adds a single element
fruits.update(["mango", "grape"]) # Adds multiple elements from an iterable

# Removing elements
fruits.remove("banana")    # Removes "banana" (Raises KeyError if not found)
fruits.discard("pear")     # Removes "pear" if present (Safe: no error if missing)

print("Fruits set:", fruits)
print("Is apple in set?", "apple" in fruits) # Fast membership test (O(1))
