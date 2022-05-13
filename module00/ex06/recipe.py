# cookbook = {'sandwich': {'ingredients': [ham, bread, cheese, tomatoes],
#                        'meal': 'lunch',
#                        'prep_time': 10},
#             'cake': {'ingredients': [flour, sugar, eggs],
#                        'meal': 'dessert',
#                        'prep_time': 60},
#             'salad': {'ingredients': [avocado, arugula, tomatoes, spinach],
#                        'meal': 'lunch',
#                        'prep_time': 15}}

# Creation of an empty dictionary
cookbook = {}

# Create lists of key:value for recipes
sandwich = [['ingredients', [ham, bread, cheese, tomatoes]], ['meal', lunch], [prep_time, 10]]
cake = [['ingredients', [flour, sugar, eggs]], ['meal', dessert], [prep_time, 60]]
salad = [['ingredients', [avocado, arugula, tomatoes, spinach]], ['meal', lunch], [prep_time, 15]]

print("1 - Creation of cookbook")
print(cookbook)



dict= {} # create an empty dictionary
list= [['a', 1], ['b', 2], ['a', 3], ['c', 4]]
#list is our input where 'a','b','c', are keys and 1,2,3,4 are values
for i in range(len(list)):
     if list[i][0] in dic.keys():# if key is present in the list, just append the value
         dic[list[i][0]].append(list[i][1])
     else:
         dic[list[i][0]]= [] # else create a empty list as value for the key
         dic[list[i][0]].append(list[i][1]) # now append the value for that key