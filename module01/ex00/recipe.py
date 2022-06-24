class Recipe:
    '''This class contains attributes that define a recipe'''

    # Initialize the attributes of the Recipe class
    def __init__(self,
                 name,
                 cooking_lvl,
                 cooking_time,
                 ingredients,
                 description,
                 recipe_type):

        # Check the name value
        self.name = name
        if (isinstance(name, str) is False):
            raise TypeError("Name must be an string !")
        if (len(name) <= 0):
            raise ValueError("Recipe must have a name !")

        # Check the cooking_lvl value
        if (isinstance(cooking_lvl, int) is False):
            raise TypeError("Cooking level must be an int !")
        if (cooking_lvl > 0 and cooking_lvl < 6):
            self.cooking_lvl = cooking_lvl
        else:
            raise ValueError("Cooking level must be between 1 and 5 !")

        # Check the cooking_time value
        if (isinstance(cooking_time, int) is False):
            raise TypeError("Cooking time must be an int !")
        if (cooking_time > 0):
            self.cooking_time = cooking_time
        else:
            raise ValueError("Cooking time must be greater than 0!")

        # Check the ingredients list
        self.ingredients = ingredients
        if (isinstance(ingredients, list) is False):
            raise TypeError("Ingredients must be a list !")
        if (len(ingredients) <= 0):
            raise ValueError("Ingredients list must contain at least 1 ingredient !")
        for elem in ingredients:
            if (isinstance(elem, str) is False):
                raise TypeError("Each ingredient must be a string !")

        # Check the description value
        self.description = description
        if (isinstance(description, str) is False):
            raise TypeError("Description must be a string !")

        # Check the recipe_type value
        self.recipe_type = recipe_type
        if (isinstance(recipe_type, str) is False):
            raise TypeError("Type must be a str !")
        if (recipe_type != ("starter" or "lunch" or "dessert")):
            raise ValueError("Type must be starter, lunch or dessert !")

    def __str__(self):
        """Return a string showing the recipe info"""

        s1 = "Name of the recipe    : {0}\n".format(self.name)
        s2 = "Cooking level         : {0}\n".format(self.cooking_lvl)
        s3 = "Cooking time          : {0}\n".format(self.cooking_time)
        s4 = "Ingredients           : {0}\n".format(self.ingredients)
        s5 = "Description           : {0}\n".format(self.description)
        s6 = "Type                  : {0}".format(self.recipe_type)
        txt = s1 + s2 + s3 + s4 + s5 + s6
        return txt
