import sys 

def count_n_arg():
    arg_list = sys.argv
    n_arg = len(arg_list)
    return n_arg


def get_user_input():
    print('Please select an option:')
    user_input = input()
    return user_input


def print_menu():
    print('================================')
    print('Welcome to the Python Cookbook !')
    print('List of available options:')
    print('1: Add a recipe')
    print('2: Delete a recipe')
    print('3: Print a recipe')
    print('4: Print the cookbook')
    print('5: Quit')
    print('================================')


def add_recipe(recipes, data):
    print('================================')
    print('Please enter the name of the recipe to add:')
    name = input()
    recipes.append(name)
    # create a new_recipe dict
    new_recipe = {}
    print('================================')
    print('Please enter ingredients of the recipe:')
    ingredients = []
    while True:
        ingredient = input()
        if ingredient == '':
            break
        else:
            ingredients.append(ingredient)
    print('================================')
    print('Please enter the meal type of the recipe:')
    meal_type = input()
    while True:
        print('================================')
        print('Please enter the preparation time of the recipe:')
        prep_time = input()
        if input_is_int(prep_time) is True and int(prep_time) > 0:
            break
        else:
            print('Preparation time should be a non-negative integer')
    # add ingredients, meal and prep_time to new_recipe dict
    new_recipe['ingredients'] = ingredients
    new_recipe['meal'] = meal_type
    new_recipe['prep_time'] = prep_time
    # add new_recipe dict to data list, then zip recipes and data lists
    data.append(new_recipe)
    new_recipe = dict(zip(recipes, data))
    return new_recipe


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
        print('Error !\nRecipe not found !')


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
        print('Error !\nRecipe not found !')


def input_is_int(str):
    if str[0] in ('-', '+'):
        return str[1:].isdigit()
    else:
        return str.isdigit()


if __name__=="__main__":
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
    if count_n_arg() > 1:
        print('Error ! Wrong number of arguments')
        print('Usage : python3 recipe.py')
    elif count_n_arg() == 1:
        option = 0
        while (option != 5):
            print_menu()
            try:
                option = int(get_user_input())
            except ValueError:
                print("Sorry, this option does not exist.\n")
            if option not in range(1, 6):
                print("Sorry, this option does not exist.\n")
            else:
                if (option == 1):
                    cookbook = add_recipe(recipes, data)
                elif(option == 2):
                    print('================================')
                    print('Please enter the name of the recipe to delete')
                    recipe_name = input()
                    cookbook = delete_recipe(recipe_name)
                elif (option == 3):
                    print('================================')
                    print('Please enter the name of the recipe to see its details')
                    recipe_name = input()
                    print_recipe_details(recipe_name)
                elif (option == 4):
                    print('================================')
                    print('COOKBOOK')
                    for i in range (0, len(cookbook)):
                        print('=== RECIPE #', i, ' ===')
                        print('Name\t\t', ':', recipes[i])
                        print(print_recipe_details(recipes[i]))

        print('Cookbook closed. Goodbye !')
        print('================================')
