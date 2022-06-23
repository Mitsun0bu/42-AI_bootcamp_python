class Recipe:
    '''This class contains attributes that define a recipe'''

    def __init__(self,
                 name,
                 cooking_lvl,
                 cooking_time,
                 ingredients,
                 description,
                 recipe_type):

        try:
            isinstance(name, str)
        except TypeError:
            print("Name must be an string !")
        self.name = name
        if (len(name) <= 0):
            raise ValueError("Recipe must have a name !")

        try:
            isinstance(cooking_lvl, int)
        except TypeError:
            print("Cooking lvl must be an int !")
        if (cooking_lvl > 0 and cooking_lvl < 6):
                self.cooking_lvl = cooking_lvl
        else:
            raise ValueError("Cooking lvl must be between 1 and 5 !")

        try:
            isinstance(cooking_time, int)
        except TypeError:
            print("Cooking time must be an int !")
        self.cooking_time = cooking_time

        try:
            isinstance(ingredients, list)
        except TypeError:
            print("Ingredients must be a list !")
        self.ingredients = ingredients

        self.description = description

        try:
            isinstance(recipe_type, str)
        except TypeError:
            print("Type must be a str !")
        try:
            recipe_type == ("starter" or "lunch" or "dessert")
        except ValueError:
            print("Type must be starter, lunch or dessert !")
        self.recipe_type = recipe_type

    def __str__(self):
        """Return a string showing the recipe info"""
        txt = '''\
Name of the recipe	: {0}
Cooking level           : {1} / 5
Cooking time            : {2} minutes
Ingredients             : {3}
Description             : {4}
Type                    : {5}'''.format(
            self.name,
            self.cooking_lvl,
            self.cooking_time,
            self.ingredients,
            self.description,
            self.recipe_type)
        return txt
