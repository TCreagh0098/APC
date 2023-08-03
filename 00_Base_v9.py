import math
import pandas as pd


# checks that the user enters either yes or no
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")


# checks that the user enters a number
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = input(question)

            if response == "?":
                return response

            response = num_type(response)

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# checks which shape the user wishes to calculate
def shape_checker(question):
    while True:
        response = input(question).lower()

        if response in ["1", "t", "triangle"]:
            return "triangle"

        elif response in ["2", "s", "square"]:
            return "square"

        elif response in ["3", "r", "rectangle"]:
            return "rectangle"

        elif response in ["4", "c", "circle"]:
            return "circle"

        elif response in ["5", "o", "oval"]:
            return "oval"

        else:
            print("Please enter a valid integer or shape name!")


# converts a number to a specified significant figure
def significant_figure(number, significant_figures):
    if number == 0:
        return 0
    return round(number, significant_figures - int(math.floor(math.log10(abs(number)))) - 1)


# finds the area and perimeter of a triangle
def choice_triangle():
    while True:
        base_triangle = num_check("Enter the base length: ", "Please enter a valid positive number (e.g., 4): ", float)
        side_a_triangle = num_check("Enter the length of side a: ", "Please enter a valid positive number (e.g., 4): ",
                                    float)
        side_b = num_check("Enter the length of side b: ", "Please enter a valid positive number (e.g., 4): ", float)

        # Check if sides form a triangle
        if base_triangle + side_a_triangle > side_b and side_a_triangle + side_b > base_triangle and \
                side_b + base_triangle > side_a_triangle:
            perimeter = side_a_triangle + side_b + base_triangle
            area = (base_triangle * side_a_triangle) / 2

            perimeter = significant_figure(perimeter, 4)
            area = significant_figure(area, 4)

            return perimeter, area

        else:
            print("The given sides do not form a triangle. Please enter valid side lengths.")


# finds the area and perimeter of a square or rectangle
def choice_square_or_rectangle(shape):
    length = num_check("Enter the side length: ", "Please enter a valid positive number (e.g., 4): ", float)

    if shape == "square":
        perimeter = 4 * length
        area = length * length
    else:
        width = num_check("Enter the side width: ", "Please enter a valid positive number (e.g., 4): ", float)
        perimeter = 2 * (length + width)
        area = length * width

    perimeter = significant_figure(perimeter, 4)
    area = significant_figure(area, 4)

    return perimeter, area


# finds the area and perimeter of a circle
def choice_circle():
    radius = num_check("Enter the radius: ", "Please enter a valid positive number (e.g., 4): ", float)

    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2

    perimeter = significant_figure(perimeter, 4)
    area = significant_figure(area, 4)

    return perimeter, area


# finds the area and perimeter of an oval
def choice_oval():
    radius_horizontal = num_check("Enter the radius of the horizontal axis: ",
                                  "Please enter a valid positive number (e.g., 4): ", float)
    radius_vertical = num_check("Enter the radius of the vertical axis: ", "Please enter a valid positive"
                                                                           " number (e.g., 4): ",
                                float)

    perimeter = 2 * math.pi * (3 * (radius_horizontal + radius_vertical) - math.sqrt(
        (3 * radius_horizontal + radius_vertical) * (radius_horizontal + 3 * radius_vertical)))
    area = math.pi * radius_horizontal * radius_vertical

    perimeter = significant_figure(perimeter, 4)
    area = significant_figure(area, 4)

    return perimeter, area


# main routine goes here
calculation_history = pd.DataFrame(columns=["Shape:", "Perimeter:", "Area:"])

# main routine goes here

# asks user if they want instructions
want_instructions = yes_no("Do you want to read the instructions? ")

# asks the user whether they wish to be told the instructions
if want_instructions == "yes":
    print(''' 
*** Instructions ***\n
This program works out the area and perimeter of a desired shape. 
It will ask you which shape you wish to find the area and perimeter of.
Then ask you for the values of the necessary sides needed to solve the area and perimeter.

(This information will be automatically saved in a txt file.)\n ''')

# asks user if they wish to continue with the program
continue_yes_no = yes_no("Do you wish to continue? (y/n): ")
if continue_yes_no == "yes":
    print()
else:
    print("Thank you for considering this program. Please try again!")


# asks user which shape they want to find the area and perimeter of
while True:
    shape_choice = shape_checker('''
Please enter which shape you wish to find the area and perimeter of:
    
1. Triangle (Must have all three sides...)
2. Square (Must have at least one side...)
3. Rectangle (Must have the length and width...)
4. Circle (Must have radius...)
5. Oval (Must have horizontal and vertical radius...)

Select shape: ''')

    if shape_choice == "triangle":
        perimeter, area = choice_triangle()

    elif shape_choice in ["square", "rectangle"]:
        perimeter, area = choice_square_or_rectangle(shape_choice)

    elif shape_choice == "circle":
        perimeter, area = choice_circle()

    elif shape_choice == "oval":
        perimeter, area = choice_oval()

    else:
        print("Invalid choice! Please enter a valid shape.")

    # Format the perimeter and area to 4 significant figures
    perimeter = significant_figure(perimeter, 4)
    area = significant_figure(area, 4)

    calculation_history.loc[len(calculation_history)] = [shape_choice.capitalize(), perimeter, area]

    heading_txt = "\n***** AREA PERIMETER CALCULATOR *****"
    perimeter_heading = "Perimeter:"
    perimeter_txt = f"Your Perimeter is: {perimeter} units (rounded to 2 significant figures)"
    area_heading = "Area:"
    area_txt = f"Your Area is: {area} units squared (rounded to 2 significant figures)"
    choice_txt = f"**** You chose: {shape_choice.capitalize()} ****"
    file_txt = f"\n(This information has been automatically saved to a txt file named <{shape_choice}.txt>)"
    thank_you_txt = f'''
------------'''

    print(heading_txt)
    print(choice_txt)
    print(perimeter_heading)
    print(perimeter_txt)
    print(area_heading)
    print(area_txt)
    print()

    if yes_no("\nDo you wish to continue using the program? (y/n): ") == "no":
        print("\nThank you for using this program!")
        break

# Write the calculation history to a text file
calculation_history_txt = "\n**** Calculation History ****\n\n" + calculation_history.to_string(index=False)
with open("calculation_history.txt", "w") as text_file:
    text_file.write(calculation_history_txt)

print(calculation_history_txt)