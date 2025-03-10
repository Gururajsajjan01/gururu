# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Add an element
set1.add(6)
print("Set 1 after adding 6:", set1)

# Remove an element
set1.remove(2)  # Raises error if element doesn't exist
print("Set 1 after removing 2:", set1)

# Discard an element (no error if element not found)
set1.discard(10)

# Set operations
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# Check membership
print("Is 3 in set1?", 3 in set1)

# Length of set
print("Length of set1:", len(set1))

# Convert list to set
list1 = [1, 2, 2, 3, 3, 3]
unique_items = set(list1)
print("Unique items from list:", unique_items)
