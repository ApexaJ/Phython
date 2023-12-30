# ## 💻 Exercises: Day 8

# 1. Create  an empty dictionary called dog
dog={}
print(dog)

# 2. Add name, color, breed, legs, age to the dog dictionary
dog={
    'name':'Lucy',
    'color':'Black',
    'Breed':'German Shepherd',
    'legs':4,
    'age':7
}
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={
    'first_name':'Apexa',
      'last_name':'Gotecha',
       'gender':'Female',
         'age':19,
           'marital status':'Unmarried',
             'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
               'country':'India',
                 'city':'Junagadh',
                     'address':' Motibag Junagadh' 
}
print(student)

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
#print(student['skills'])
if type(student['skills'])==list:
    print("yes,it is")
else:
    print("no it doesn't")

# 6. Modify the skills values by adding one or two skills
    student['skills'][0]='coordinatation'
    print(student['skills'])

# 7. Get the dictionary keys as a list
print(student.keys())

# 8. Get the dictionary values as a list
print(student.values())

# 9. Change the dictionary to a list of tuples using _items()_ method
tuple_list=list(student.items())
print(tuple_list)

# 10. Delete one of the items in the dictionary
print(student.pop('marital status'))
print(student)

# 11. Delete one of the dictionaries
del dog
print(student)