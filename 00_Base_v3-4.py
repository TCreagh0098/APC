import math


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
            response = num_type(input(question))

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


# asks the user whether they wish to be told the instructions
def instructions_yes_no():
    want_instructions = yes_no("Do you want to read the instructions? ")

    if want_instructions == "yes":
        print(''' 
*** Instructions ***\n
This program works out the area and perimeter of a desired shape. 
It will ask you which shape you wish to find the area and perimeter of.
Then ask you for the values of the necessary sides needed to solve the area and perimeter.

(This information will be automatically saved in a txt file.)\n ''')


# checks with the user whether they understand the instructions and if they wish to continue
def continue_yes_no(question):
    while True:
        response = input(question).lower()
        error = "Please enter yes or no!"

        if response == "yes" or response == "y":
            break

        elif response == "no" or response == "n":
            print("\nThank you for considering this program!")
            quit()

        else:
            print(error)


# converts a number to a specified significant figure
def significant_figure(number, significant_figures):
    if number == 0:
        return 0
    return round(number, significant_figures - math.floor(math.log10(abs(number))) - 1)


# finds the area and perimeter of a triangle
def choice_triangle():
    base_triangle = num_check("Enter the base length: ", "Please enter a valid positive number (e.g., 4): ", float)
    side_a_triangle = num_check("Enter the length of side a: ", "Please enter a valid positive number (e.g., 4): ", float)
    side_b = num_check("Enter the length of side b: ", "Please enter a valid positive number (e.g., 4): ", float)

    perimeter = side_a_triangle + side_b + base_triangle
    area = (base_triangle * side_a_triangle) / 2

    perimeter = significant_figure(perimeter, 4)
    area = significant_figure(area, 4)

    return perimeter, area


# finds the area and perimeter of a square
def choice_square():
    side_square = num_check("Enter the side length: ", "Please enter a valid positive integer e.g. 4", float)

    perimeter = 4 * side_square
    area = side_square ** 2

    perimeter = significant_figure(perimeter, 4)
    area = significant_figure(area, 4)

    return perimeter, area


# finds the area and perimeter of a rectangle
def choice_rectangle():
    length_rectangle = num_check("Enter the length of your rectangle: ", "Please enter a valid positive integer e.g. 4",
                                 float)
    width_rectangle = num_check("Enter the width of your rectangle: ", "Please enter a valid positive integer e.g. 4",
                                float)

    perimeter = 2 * (length_rectangle + width_rectangle)
    area = length_rectangle * width_rectangle

    perimeter = significant_figure(perimeter, 4)
    area = significant_figure(area, 4)

    return perimeter, area


# finds the area and perimeter of a circle
def choice_circle():
    radius = num_check("Enter the radius of the circle: ", "Please enter a valid positive number (e.g., 4): ", float)

    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2

    perimeter = significant_figure(perimeter, 4)
    area = significant_figure(area, 4)

    return perimeter, area


# finds the area and perimeter of a oval
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

# asks user if they want instructions
instructions_yes_no()

# asks user if they wish to continue with the program
continue_yes_no("Do you understand and wish to continue? (y/n): ")

# determines and returns which shape the user wishes
shape_choice = shape_checker('''\nPlease enter which shape you wish to find the area and perimeter of:
 
1. Triangle
2. Square
3. Rectangle
4. Circle
5. Oval 

Select shape: ''')

# asks user what values their values are based on what shape they chose
if shape_choice == "triangle":
    perimeter, area = choice_triangle()

elif shape_choice == "square":
    perimeter, area = choice_square()

elif shape_choice == "rectangle":
    perimeter, area = choice_rectangle()

elif shape_choice == "circle":
    perimeter, area = choice_circle()

elif shape_choice == "oval":
    perimeter, area = choice_oval()

else:
    print("Invalid choice! Please enter a valid shape.")


heading_txt = "\n***** AREA PERIMETER CALCULATOR *****"
perimeter_heading = "Perimeter:"
perimeter_txt = f"Your Perimeter is: {perimeter} units (rounded to 2 significant figures)"
area_heading = "Area:"
area_txt = f"Your Area is: {area} units squared (rounded to 2 significant figures)"
choice_txt = f"**** You chose: {shape_choice} ****"
file_txt = f"\n(This information has been automatically saved to a txt file named <{shape_choice}.txt>)"
thank_you_txt = f'''
------------
\nThank you for choosing this program to find the area and perimeter of your {shape_choice}! \
Please use this again!'''

to_write = [heading_txt, choice_txt, perimeter_heading, perimeter_txt, area_heading, area_txt, thank_you_txt, file_txt]

# Write to file...
# create file to hold data (add .txt extension)
file_name = f"{shape_choice}.txt"
text_file = open(file_name, "w+")

# heading
for item in to_write:
    text_file.write(str(item))
    text_file.write("\n\n")

# close file
text_file.close()

# Print Stuff
for item in to_write:
    print(item)
    print()
