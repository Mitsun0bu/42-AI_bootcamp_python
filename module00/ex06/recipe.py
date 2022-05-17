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


cookbook = {}
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
