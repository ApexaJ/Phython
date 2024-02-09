#A)
Language=["java","python","php","React","Express"]
print("Original List:",Language)
#Append String
Language.append("Mongo")
print("After Append:",Language)
# Extend String
Language.extend([".Net","C++","C#"])
print("After Extend:",Language)
# Remove From String
Language.remove("C#")
print("After Remove:",Language)
# Reverse String
Language.reverse()
print("After Reverse:",Language)
# Sort String in Ascending Order
Language.sort()
print("List in Ascending Order:",Language)
# Sort String in Decending Order
Language.sort(reverse=True)
print("List in Decending Order:",Language)

#B)
list1 = [1, 2, 3, 4, ["python", "java", "c++", [10, 20, 30]], 5, 6, 7, ["apple", "banana", "orange"]]
print("Original List:",list1)
# Get word Orange
word_orange = list1[-1][-1][-1]
# Get word Python
word_python = list1[4][0].capitalize()  # Capitalize first letter to match "Python"

print("Word 'orange':", word_orange)
print("Word 'Python':", word_python)
# Repeat list 5 times
repeat_list=[list1]*5 
print("Repeated List is:",repeat_list)
print("Repeated List is:\n", '\n'.join(map(str, repeat_list)))

#C)

# Create a list
original_list = [2, 4, 6, 8, 10]

# Copy the list using the slice function
copied_list = original_list[:]

# Display the original and copied lists
print("Original List:", original_list)
print("Copied List:", copied_list)

#D)
# Create a tuple
my_tuple = (3, 8, 5, 2, 10)

# Calculate the sum of elements in the tuple
sum_result = sum(my_tuple)

# Find the maximum and minimum values in the tuple
max_value = max(my_tuple)
min_value = min(my_tuple)

# Display the results
print("Tuple:", my_tuple)
print("Sum:", sum_result)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)
