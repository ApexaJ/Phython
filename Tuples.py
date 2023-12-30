# ### Exercises: Level 1

# 1. Create an empty tuple
empty_tuple = ()
print(empty_tuple)

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters=('Isha','Vidhi','Bansi','Diya','Khushi','Nidhi','Gyani')
brothers=('Brij','Hitarth','Raj','Darshan')
print(sisters)
print(brothers)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings=sisters+brothers
print(siblings)

# 4. How many siblings do you have?
total=len(siblings)
print(total)

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# siblings=list(siblings)
# siblings[0]='JitendraBhai'
# siblings[1]='RekhaBen'
# siblings=tuple(siblings)
# family_members=siblings
parents=('JitendraBhai','RekhaBen')
family_members=(parents),(siblings)
print(family_members)

### Exercises: Level 2

# 1. Unpack siblings and parents from family_members
(parents),(siblings)=(family_members)
print(parents)
print(siblings)

# print(family_members)
print(family_members)

# 1. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('Mango','Guava','Kiwi','Apple','Orange')
vegetables=('potato','Brinjal','Lemon','Tomato','Sweet Potato')
animal=('Lion','Elephant','Tiger','Rabbit','Dog')
food_staff_tp=(fruits+vegetables+animal)
print(food_staff_tp)

# 1. Change the about food_stuff_tp  tuple to a food_stuff_lt list
food_staff_lt=food_staff_tp
print(food_staff_lt)

# 1. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid=int(len(food_staff_lt)/2)
print(food_staff_lt[mid:mid+3])

# 1. Slice out the first three items and the last three items from food_staff_lt list
first=food_staff_lt[0:3]
print(first)
last=food_staff_lt[-3:]
print(last)

# 1. Delete the food_staff_tp tuple completely
del food_staff_lt

# 1. Check if an item exists in  tuple:
# - Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries)
if "Estoin" in nordic_countries:
    print("yes it exists")
else:
    print("No it doesn't exist")

# - Check if 'Iceland' is a nordic country
print(nordic_countries)
if "Iceland" in nordic_countries:
    print("yes it exists")
else:
    print("No it doesn't exist")