'''
Yingshu Wang
CS5001 Fall 2021

The program is to enable users to save and read recipes.
'''


def write_recipe_to_file(name_recipe, ingredient, time, direction):
    '''
    Function -- write_recipe_to_file
        Write recipe to file following a format
    Parameters:
        name_recipe -- String type, recipe name after validation
        ingredient -- A string of ingredient. Validation of the name needed.
        time -- Integer number. Minutes unit.
        direction -- Detailed direction of cooking.
    Returns:
        Save a txt file in relative path with name of name_recipe.txt.
    '''
    filename = name_recipe + ".txt"
    with open(filename, 'w') as file:
        file.write(name_recipe + "\n")
        file.write("\n")
        file.write("Ingredients:\n")
        ingredient_ele = ingredient.split(",")
        for element in ingredient_ele:
            file.write(element + "\n")
        file.write("\n")
        file.write("Time: {} minutes\n".format(time))
        file.write("\n")
        file.write("Directions:\n")
        file.write(direction)


def convertFilename(recipe_name):
    '''
    Function -- confertFilename
        Convert recipe name to file name
    Parameters:
        recipe_name -- String type, recipe name
    Returns:
        A string that follows rules
    '''
    filename_1 = recipe_name.lower().strip()
    if " " in filename_1:
        filename_1 = filename_1.replace(" ", "_")
    if not filename_1.isalnum():
        filename = ""
        for i in range(len(filename_1)):
            if filename_1[i].isalnum() or filename_1[i] == "_":
                filename += filename_1[i]
        return filename
    else:
        return filename_1


def isListEmpty(ingredient):
    '''
    Function -- isListEmpty
        Check if a string is empty. All elements of list coming from the
        string are empty.
    Parameters:
        ingredient -- A string. The elements of the string are seperated by
        comma.
    Returns:
        True if empty. Otherwise, False.
    '''
    ingredient_ele = ingredient.split(",")
    non_emp_count = 0
    for element in ingredient_ele:
        if element.strip() != "":
            non_emp_count += 1
    if non_emp_count == 0:
        return True
    else:
        return False


def main():
    isLoop = True
    while isLoop:
        menu_msg = "MENU: 1 - Save a new recipe, 2 - Read a recipe, 3 - Quit "
        choose = input(menu_msg)
        QUIT = 3
        SAVE_NEW_RECIPT = 1
        try:
            choose_update = int(choose)
            if choose_update < 1 or choose_update > 3:
                raise IndexError("The index is out of range")
            elif choose_update == QUIT:
                isLoop = False
            elif choose_update == SAVE_NEW_RECIPT:
                ingredient_msg = ("Enter the ingredients on one line." +
                                  " Separate each ingredient with a comma. ")
                ingredient = input(ingredient_msg)
                ingreLoop = True
                while ingreLoop:
                    if isListEmpty(ingredient):
                        print("Recipe must have at least one ingredient.")
                        ingredient = input(ingredient_msg)
                    else:
                        break
                direction = input("Enter the directions (1 paragraph only): ")
                time_need = input("Enter the time needed in minutes: ")
                validTimeLoop = True
                enter_time_msg = "Enter the time needed in minutes: "
                while validTimeLoop:
                    invalid_time_msg = ("Invalid time. Must be an integer " +
                                        "greater than or equal to 0.")
                    try:
                        if int(time_need) < 0:
                            print(invalid_time_msg)
                            time_need = input(enter_time_msg)
                        else:
                            time = int(time_need)
                            break
                    except ValueError:
                        print(invalid_time_msg)
                        time_need = input(enter_time_msg)
                name_recipe = input("Enter a name for the recipe: ")
                if convertFilename(name_recipe) == "":
                    print("Unable to create the filename.")
                    isEnterFileLoop = True
                    while isEnterFileLoop:
                        file_update_msg = ("Enter a string containing only" +
                                           " letters, numbers, and spaces ")
                        fileNameUpdate = input(file_update_msg)
                        file_name = convertFilename(fileNameUpdate)
                        if file_name != "":
                            isEnterFileLoop = False
                else:
                    file_name = convertFilename(name_recipe)
                write_recipe_to_file(file_name, ingredient, time, direction)
                save_msg = (name_recipe + " recipe saved to " +
                            file_name + ".txt")
                print(save_msg)
            else:
                reading_recipe_name = input("Enter the name of the recipe: ")
                reading_file_name = convertFilename(reading_recipe_name)
                filename = reading_file_name + ".txt"
                try:
                    with open(filename, 'r') as file:
                        for line in file:
                            print(line.strip())
                except FileNotFoundError:
                    print("Unable to read {}".format(filename))
        except Exception:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
