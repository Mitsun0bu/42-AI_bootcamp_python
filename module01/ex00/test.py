import os
import datetime
from book import Book
from recipe import Recipe


recipe_1 = Recipe("sandwich",
                  1,
                  5,
                  ["bread", "ham", "cheese", "salad"],
                  "A quick, simple and delicious meal !",
                  "lunch")
print(str(recipe_1))

print("\n")

recipe_2 = Recipe("soup",
                  2,
                  15,
                  ["bread", "ham", "cheese", "salad"],
                  "An easy way to eat a lot of veggetables !",
                  "lunch")
print(str(recipe_2))

print("\n")

path = "test.py"

modif_ts = os.path.getmtime(path)
creation_ts = os.path.getctime(path)

book_1 = Book("cookbook",
              datetime.datetime.fromtimestamp(modif_ts),
              datetime.datetime.fromtimestamp(creation_ts),
              {recipe_1.recipe_type: recipe_1.name,
               recipe_2.recipe_type: recipe_2.name})
print(str(book_1))
