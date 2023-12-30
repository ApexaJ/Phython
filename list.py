# 1. Declare an empty list
empty_list =list()
print(empty_list)

# 2. Declare a list with more than 5 items
Fruits = ['Banana','Orange','Mango','Lemon','Apple','Guava','Pineapple']
print('Fruits:',Fruits)

# 3. Find the length of your list
print(len(Fruits))

# 4. Get the first item, the middle item and the last item of the list
first_fruit=Fruits[0]
print((first_fruit))
last_fruit = Fruits[6]
print(last_fruit)
mid=int(len(Fruits)/2)
print(Fruits[mid])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types =['Apexa',19,5.0,'Unmarried','Hostel']
print(mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)

# 7. Print the list using _print()_
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
first =it_companies[0]
print((first))
last= it_companies[6]
print((last))
mid=int(len(it_companies)/2)
print(it_companies[mid])

# a='string'
# b='5'
# print(a*5-b)

# 10. Print the list after modifying one of the companies
it_companies[6]="boat"
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Delloite Consulting')
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(6,"TCS")
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
# upper= it_companies.upper(2,"Microsoft")
# it_companies.upper(2,'Microsoft')
# print(it_companies)
uppercase= it_companies[2].upper()
print(uppercase)

# 14. Join the it_companies with a string '#;&nbsp; '
Join1 = "#;&nbsp;".join(it_companies)
print(Join1)

# 15. Check if a certain company exists in the it_companies list.
does_exist= 'Google' in it_companies
print(does_exist)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
compnies=it_companies[0:3]
print(compnies)

# 19. Slice out the last 3 companies from the list
compnies1=it_companies[-3:]
print(compnies1)

# 20. Slice out the middle IT company or companies from the list
mid=int(len(it_companies)/2)
print(it_companies[mid:mid+3])

# 21. Remove the first IT company from the list
# remove1=it_companies.remove[0]
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company or companies from the list
mid=int(len(it_companies)/2)
remove2=it_companies.pop(mid)
print(remove2)

# 23. Remove the last IT company from the list
it_companies.pop(6)
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end)
print(back_end)
join1=front_end+back_end
print(join1)


# ### Exercises: Level 2

# 1. The following is a list of 10 students ages:

# ```sh
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ```
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)


# - Sort the list and find the min and max age
ages.sort()
print(ages)
# - Add the min age and the max age again to the list
ages.append(19)
print(ages)
ages.append(26)
print(ages)

# - Find the median age (one middle item or two middle items divided by two)
mid=int(len(ages)/2)
print(ages[mid]/2)

# - Find the average age (sum of all items divided by their number )
average=sum(ages)/len(ages)
print(average)

# - Find the range of the ages (max minus min)
range=max(ages)-min(ages)
print(range)

# - Compare the value of (min - average) and (max - average), use _abs()_ method
abs=(max(ages)-average)
print(abs)
abs=(min(ages)-average)
print(abs)

# 1. Find the middle country(ies) in the [countries list]
countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(countries)
mid=int(len(countries)/2)
print(countries[mid])

# 1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_list=(countries[:mid])
print(first_list)
second_list=(countries[mid:])
print(second_list)

# 1. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
print(first_list)
scandic_countries=second_list
print(scandic_countries)
