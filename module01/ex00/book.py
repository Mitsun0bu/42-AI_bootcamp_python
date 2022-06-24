from datetime import datetime


class Book:
    '''This class contains attributes that define a book'''

    # Initialize the attributes of the Book class
    def __init__(self,
                 name,
                 last_update,
                 creation_date,
                 recipes_list):

        # Check the name value
        self.name = name
        if (isinstance(name, str) is False):
            raise TypeError("Name must be an string !")
        if (len(name) <= 0):
            raise ValueError("Recipe must have a name !")

        # Check the last_update value
        self.last_update = last_update
        if (isinstance(last_update, datetime) is False):
            raise TypeError("Last update must have datetime type !")

        # Check the creation_date value
        self.creation_date = creation_date
        if (isinstance(creation_date, datetime) is False):
            raise TypeError("Creation date must have datetime type !")

        # Check the recipes_list value
        self.recipes_list = recipes_list
        if (isinstance(recipes_list, dict) is False):
            raise TypeError("The list of recipes must be a dict !")
        for key in recipes_list.keys():
            if (key != ("starter" or "lunch" or "dessert")):
                raise ValueError("Recipe type must be starter, lunch or dessert !")
