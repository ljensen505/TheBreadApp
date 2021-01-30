def print_intro():
    """
    This function prints the introductory comments for the user to read.
    INPUT: none
    OUTPUT: Intro
    """
    print("Welcome to the Bread App!\nI'll convert a conventional bread recipe into a sourdough recipe.  A couple things to keep in mind:")
    print("\tYour original recipe's suggested timing won't work anymore, so use volume of your dough to determine when it's ready.")
    print("\tFeed your starter about 24hrs before making your Levain.")
    print("\tUsing milk is not recommended because of a very slow rise.")
    print("\tEverything should be in grams. Both what I tell you, and what you tell me.")
    print("\nLet's start with your original (commercial yeast) recipe.")
    return


def positive_responses():
    """
    This function returns a list of positive responses
    INPUT: none
    OUTPUT: positive responses
    """
    return ['yes', 'y', 'yeah']



def negative_responses():
    """
    This function returns a list of negative responses
    INPUT: none
    OUTPUT: positive responses
    """
    return ['no', 'n', 'nope']


def get_weight(ingredient):
    """
    USAGE: gets user input in grams of a specified ingredient
    INPUT: ingredient name
    OUTPUT: integer of ingredient weight based upon user input
    """
    error_message = 'Usage: "1000g" or "1000"; not "thousand" or " ".'

    while True:
        weight = input(f"\tHow much {ingredient}: ")

        weight_list = [char for char in weight]
        number_exists = False

        for char in weight_list:
            if ord(char) >= 48 and ord(char) <= 57:
                number_exists = True
                
        if not weight: # was there actually user input?
            print(error_message)
            continue
        elif not number_exists: # did the user input contain a number?
            print(error_message)
            continue
        else:
            number_list = []
            for char in weight_list:
                if ord(char) >= 48 and ord(char) <= 57:
                    number_list.append(char)
            weight_int = int(''.join(number_list))
            return weight_int
    
