def print_recipes_names(cookbook):
    for recipe in recipes:
        print(recipe)


def print_recipe_details(recipe_name):
    key_list = list(cookbook.keys())
    value_list = list(cookbook.values())
    found = False
    for i in range(0, len(key_list)):
        if key_list[i] == recipe_name:
            print('Ingredients list :', value_list[i]['ingredients'])
            print('To be eaten for  :', value_list[i]['meal'])
            print('Preparation time :', value_list[i]['prep_time'])
            found = True
    if found is False:
        print('Recipe not found !')


def delete_recipe(recipe_name):
    hashable_cookbook = [(key, value) for key, value in cookbook.items()]
    i_to_del = -1
    for i_recipe in range(len(hashable_cookbook)):
        if hashable_cookbook[i_recipe][0] == recipe_name:
            i_to_del = i_recipe
    if i_to_del != -1:
        hashable_cookbook.pop(i_to_del)
        new_cookbook = dict(hashable_cookbook)
        return new_cookbook
    else:
        print('Recipe not found !')


def input_is_int(str):
    if str[0] in ('-', '+'):
        return str[1:].isdigit()
    else:
        return str.isdigit()


def add_recipe(recipes, data):
    # get name of the new_recipe and add it to recipes list
    print('Enter a name:')
    name = input()
    recipes.append(name)
    # create a new_recipe dict
    new_recipe = {}
    # get ingredients list
    print('Enter ingredients:')
    ingredients = []
    while True:
        ingredient = input()
        if ingredient == '':
            break
        else:
            ingredients.append(ingredient)
    # get meal type
    print('Enter a meal type:')
    meal_type = input()
    # get preparation time
    print('Enter a preparation time:')
    while True:
        prep_time = input()
        if input_is_int(prep_time) is True and int(prep_time) > 0:
            break
        else:
            print('Preparation time should be a non-negative integer')
            print('Enter a preparation time:')
    # add ingredients, meal and prep_time to the new_recipe dict
    new_recipe['ingredients'] = ingredients
    new_recipe['meal'] = meal_type
    new_recipe['prep_time'] = prep_time
    # add the new_recipe to data list
    data.append(new_recipe)
    # zip recipes and data lists in new_recipe dict, then return it
    new_recipe = dict(zip(recipes, data))
    return new_recipe


recipes = ['sandwich', 'cake', 'salad']
data = [{'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
         'meal': 'lunch',
         'prep_time': 10},
        {'ingredients': ['flour', 'sugar', 'eggs'],
         'meal': 'dessert',
         'prep_time': 60},
        {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
         'meal': 'lunch',
         'prep_time': 15}]
cookbook = dict(zip(recipes, data))


# ~~~~~ TESTS ~~~~~
# print_recipes_names(cookbook)
# print('\n')
# print_recipe_details('salad')
# print('\n')
# cookbook = delete_recipe('cake')
# print('\n')
# cookbook = add_recipe(recipes, data)
# print('\n')
# print(cookbook)
