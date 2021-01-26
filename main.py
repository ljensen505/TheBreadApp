# BUGS TO FIX
# include starter flour/water in total amounts
# fix negative ww flour when no ww flour called for

import re

print("Welcome to the Bread App!\nI'll convert a conventional bread recipe into a sourdough recipe.  A couple things to keep in mind:")
print("\tYour original recipe's suggested timing won't work anymore, so use volume of your dough to determine when it's ready.")
print("\tFeed your starter about 24hrs before making your Levain.")
print("\tEverything should be in grams. Both what I tell you, and what you tell me.")
input("\nLet's start with your original (conventional yeast) recipe. Press 'enter' when you're ready.")

original_recipe = {
    "APflour": int(re.sub("[^0-9]", "", input("\tHow much AP flour: "))),
    "WWflour": int(re.sub("[^0-9]", "", input("\tHow much WW flour: "))),
}

flour_total = original_recipe['APflour'] + original_recipe['WWflour']

# Are there any other flours used?
other_flours = True
while other_flours:
    answer = (input("Do you need to add any additional types of flour: ").lower())
    if answer == 'yes' or answer == 'y':
        # Gather info for additional flours
        new_flour_name = input("\tFlour type: ")
        new_flour_mass = int(re.sub("[^0-9]", "", input("\tAmount: ")))
        original_recipe[new_flour_name] = new_flour_mass
        flour_total += new_flour_mass
    elif answer == 'no' or answer == 'n':
        other_flours = False
    else:
        print("Please make a valid entry (yes/no).")

original_recipe['water'] = int(re.sub("[^0-9]", "", input("\tHow much water: ")))
original_recipe['salt'] = int(re.sub("[^0-9]", "", input("\tHow much salt: ")))

# Are there any other ingredients besides flour, water, or salt?
other_ingredients = True
while other_ingredients:
    answer = (input("Any other ingredients to add: ").lower())
    if answer == 'yes' or answer == 'y':
        # Gather info for additional flours
        new_ingredient_name = input("\tIngredient name: ")
        new_ingredient_mass = int(re.sub("[^0-9]", "", input("\tAmount: ")))
        original_recipe[new_ingredient_name] = new_ingredient_mass
    elif answer == 'no' or answer == 'n':
        other_ingredients = False
    else:
        print("Please make a valid entry (yes/no).")

# Obtain and calculate scale
print(f"\nYour total original amount of flour is {flour_total}g.")
SD_flour_total = int(re.sub("[^0-9]", "", input("\nHow much total flour would you like to use in the sourdough recipe (one loaf uses about 500g): ")))

scale = SD_flour_total / flour_total
sourdough_recipe = {key:val*scale for key,val in original_recipe.items()}

# Calculate levain mass and ingredient amounts
levain_mass = SD_flour_total / 4

levain = {
    'APflour': levain_mass / 2.5,
    'WWflour': levain_mass / 10,
    'starter': levain_mass / 10,
    'water': levain_mass / 2.5,
}

# substract levain flour and water amounts from SD recipe
sourdough_recipe['APflour'] -= levain['APflour']
sourdough_recipe['WWflour'] -= levain['WWflour']
sourdough_recipe['water'] -= levain['water']

# add levain to SD recipe
sourdough_recipe['levain'] = levain_mass

# display the final sourdough recipe, including the levain
print("\nHere is your scaled and converted sourdough recipe:\n")
print(f"Levain ({levain_mass}g):")
for key,val in levain.items():
    print(f"\t{key.title()}: {round(val)}g")

print(f"\nFinal Dough:")
for key,val in sourdough_recipe.items():
    print(f"\t{key.title()}: {round(val)}g")

