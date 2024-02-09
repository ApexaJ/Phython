#A)

 # Reverse a string
original_string = "Hello, World!"
reversed_string = original_string[::-1]
print("Reversed String:", reversed_string)

# Replace a string with another string
new_string = original_string.replace("World", "Universe")
print("String after Replacement:", new_string)

# Merge two strings
string1 = "Hello"
string2 = "World"
merged_string = string1 + " " + string2
print("Merged String:", merged_string)

# Check if a character is in the string
character_to_find = "e"
is_present = character_to_find in original_string
print(f"Is '{character_to_find}' present in the string? {is_present}")

# Split string into multiple words & characters
words = original_string.split()
characters = list(original_string)
print("Split into Words:", words)
print("Split into Characters:", characters)

#B)
# Create dictionaries
dict1 = {'a': 1, 'b': 3}
dict2 = {'b': 5, 'c': 4}
dict3 = {'d': 7, 'e': 9}

# Update dictionary
dict1.update(dict2)
print("Updated Dictionary:", dict1)

# Delete key from dictionary
del dict1['a']
print("Dictionary after Delete:", dict1)

# Clear dictionary
dict1.clear()
print("Cleared Dictionary:", dict1)

# Pop item from dictionary
popped_item = dict2.popitem()
print("Popped Item:", popped_item)
print("Dictionary after Pop Item:", dict2)

# Pop specific key from dictionary
value_popped = dict3.pop('d')
print("Value Popped:", value_popped)
print("Dictionary after Pop Key:", dict3)

# Get value for a key
value = dict2.get('b', "Key not found")
print("Value for key 'b':", value)

# Display keys and values
keys = dict3.keys()
values = dict3.values()
print("Keys:", keys)
print("Values:", values)

# Merge three dictionaries into one
merged_dict = {**dict1, **dict2, **dict3}
print("Merged Dictionary:", merged_dict)
