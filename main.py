"""
ABOUT
This file contains all of the code to run a bread recipe conversion. 

BUGS TO FIX
improper handling of decimal in original recipe. 10.5g of salt -> 210g, but 10g is handled properly
"""

from bread_functions import *

print_intro()

# Begin gathering ingredients, staring with flour 
original_recipe = {
    "white flour": get_weight('white flour'),
    "whole wheat flour": get_weight('whole wheat flour'),
}

# Begin calculating original total flour weight
original_flour_total = original_recipe['white flour'] + original_recipe['whole wheat flour']

# Ask if any other flours are used
other_flours = True
while other_flours:
    answer = (input("Do you need to add any additional types of flour: ").lower())
    if answer in positive_responses():
        # Gather info for new flours
        new_flour_name = input("\tFlour type: ")
        new_flour_weight = get_weight(new_flour_name)
        # Add to original recipe dictionary
        original_recipe[new_flour_name] = new_flour_weight
        # Add new flour weight to total weight
        original_flour_total += new_flour_weight
    elif answer in negative_responses():
        other_flours = False
    else:
        print("Please make a valid entry (yes/no).")

# Begin collecting other ingredients, starting with water and salt
original_recipe['water'] = get_weight('water')
original_recipe['salt'] = get_weight('salt')

# Continue collecting other (less common) ingredients
other_ingredients = True
while other_ingredients:
    answer = input("Do you need to add any other ingredients: ").lower()
    if answer in positive_responses():
        # Gather info for new ingredients
        new_ingredient_name = input("\tIngredient name: ")
        new_ingredient_weight = get_weight(new_ingredient_name)
        # Add to original recipe dictionary
        original_recipe[new_ingredient_name] = new_ingredient_weight
    elif answer in negative_responses():
        other_ingredients = False
    else:
        print("Please make a valid entry (yes/no).")

# Obtain and calculate scale
print(f"\nYour total original flour weight is {original_flour_total}g.")
print("A typical loaf uses about 500g of flour.")
sourdough_flour_total = get_weight('total flour would you like to use')
scale = sourdough_flour_total / original_flour_total

# Calculate levain and starter weights and their ingredient weights
levain_weight = (original_flour_total * scale) / 4
starter_weight = levain_weight * (25 / 250)
starter_white_flour = starter_weight / 4
starter_whole_wheat_flour = starter_weight / 4
starter_water = starter_weight / 2

levain_recipe = {
    'white flour': levain_weight / 2.5,
    'whole wheat flour': levain_weight / 10,
    'starter': starter_weight,
    'water': levain_weight / 2.5,
}

# Create initial sourdough recipe using scale and original ingredients
sourdough_recipe = {key:val*scale for key,val in original_recipe.items()}

# substract levain (and starter) flour and water amounts from sourdough recipe
sourdough_recipe['white flour'] -= levain_recipe['white flour'] + starter_white_flour
sourdough_recipe['whole wheat flour'] -= levain_recipe['whole wheat flour'] + starter_whole_wheat_flour
sourdough_recipe['water'] -= levain_recipe['water'] + starter_water

# Handle zero whole wheat flour in original recipe.
# Since the levain will have whole wheat flour, that amount will be added to white flour
# and whole wheat flour will be set to zero
if sourdough_recipe['whole wheat flour'] < 0:
    sourdough_recipe['white flour'] += sourdough_recipe['whole wheat flour']
    sourdough_recipe['whole wheat flour'] = 0

# Calculate hydration %
hydration = (sourdough_recipe['water'] + levain_recipe['water'] + starter_water) / (original_flour_total * scale)

# Display the final sourdough, including the levain
print("\nHere is your scaled and converted sourdough recipe:\n")
print(f"Levain ({levain_weight}g):")
for key,val in levain_recipe.items():
    print(f"\t- {key.title()}: {round(val)}g")

print(f"\nFinal Dough @{hydration*100}%:")
for key,val in sourdough_recipe.items():
    print(f"\t- {key.title()}: {round(val)}g")