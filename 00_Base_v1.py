# want instructions go here
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")


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


def shape_checker():
    # asks user what shape the would like
    print("Welcome to Area and Perimeter Calculator!")
    print("Please enter which shape you wish to find the area and perimeter of: ")
    print("1. Triangle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Circle")
    print("5. Oval")

    choice_shape = num_check("Enter your choice (1-6): ", "Please enter a valid integer between 1-6", int)

def instructions_yes_no():
    want_instructions = yes_no("Do you want to read the instructions? ")

    if want_instructions == "yes":
        print(''' 
        ==== Instructions ====\n
        This program works out the area and perimeter of a desired shape. 
        It will ask you which shape you wish to find the area and perimeter of.
        Then ask you for the values of the necessary sides needed to solve the area and perimeter.
        
        This information will be automatically saved in a txt file.\n ''')


def choice_triangle():
    base_triangle = num_check("Enter the base length: ", "Please enter a valid integer e.g. 4", float)
    height_triangle = num_check("Enter the height: ", "Please enter a valid integer e.g. 4", float)
    side_a_triangle = num_check("Enter the length of side a: ", "Please enter a valid integer  e.g. 4", float)
    side_b = num_check("Enter the length of side b: ", "Please enter a valid integer e.g. 4", float)

    perimeter = side_a_triangle + side_b + base_triangle
    area = 0.5 * base_triangle * height_triangle

    return perimeter, area


def choice_square():
    side_square = num_check("Enter the side length: ", "Please enter a valid integer e.g. 4", float)

    perimeter = 4 * side_square
    area = side_square ** 2

    return perimeter, area


def choice_rectangle():
    length_rectangle = num_check("Enter the length of your rectangle: ", "Please enter a valid integer e.g. 4", float)
    width_rectangle = num_check("Enter the width of your rectangle: ", "Please enter a valid integer e.g. 4", float)

    perimeter = 2 * (length_rectangle + width_rectangle)
    area = length_rectangle * width_rectangle

    return perimeter, area


# main routine goes here

# asks user if they want instructions
instructions_yes_no()

# asks user what shape the would like
print("Welcome to Area and Perimeter Calculator!")
print("Please enter which shape you wish to find the area and perimeter of: ")
print("1. Triangle")
print("2. Square")
print("3. Rectangle")
print("4. Circle")
print("5. Oval")


choice_shape = num_check("Enter your choice (1-6): ", "Please enter a valid integer between 1-6", int)
# asks user what values they would like depending on what shape
if choice_shape == 1:
    perimeter, area = choice_triangle()


elif choice_shape == 2:
    perimeter, area = choice_square()

elif choice_shape == 3:
    perimeter, area = choice_rectangle()

else:
    print("Invalid choice! Please enter 1, 2 or 3!")

# Print the results
print("Perimeter:", perimeter)
print("Area:", area)

perimeter_txt = f"=== Your Perimeter is: {perimeter}"
area_txt = f"=== Your Area is: {area}"
choice_txt = f"=== You chose shape number: {choice_shape}"

to_write = [choice_txt, perimeter_txt, area_txt]

# Write to file...
# create file to hold data (add .txt extension)
file_name = f"{choice_shape}.txt"
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
