import math


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


def significant_figure(number, significant_figures):
    if number == 0:
        return 0
    return round(number, significant_figures - math.floor(math.log10(abs(number))) - 1)


# shape choice functions begin:
def choice_triangle():
    base_triangle = num_check("Enter the base length: ", "Please enter a valid integer e.g. 4", float)
    height_triangle = num_check("Enter the height: ", "Please enter a valid integer e.g. 4", float)
    side_a_triangle = num_check("Enter the length of side a: ", "Please enter a valid integer  e.g. 4", float)
    side_b = num_check("Enter the length of side b: ", "Please enter a valid integer e.g. 4", float)

    perimeter = side_a_triangle + side_b + base_triangle
    area = 0.5 * base_triangle * height_triangle

    perimeter = significant_figure(perimeter, 2)
    area = significant_figure(area, 2)

    return perimeter, area


def choice_square():
    side_square = num_check("Enter the side length: ", "Please enter a valid integer e.g. 4", float)

    perimeter = 4 * side_square
    area = side_square ** 2

    perimeter = significant_figure(perimeter, 2)
    area = significant_figure(area, 2)

    return perimeter, area


def choice_rectangle():
    length_rectangle = num_check("Enter the length of your rectangle: ", "Please enter a valid integer e.g. 4", float)
    width_rectangle = num_check("Enter the width of your rectangle: ", "Please enter a valid integer e.g. 4", float)

    perimeter = 2 * (length_rectangle + width_rectangle)
    area = length_rectangle * width_rectangle

    perimeter = significant_figure(perimeter, 2)
    area = significant_figure(area, 2)

    return perimeter, area


def choice_circle():
    radius = num_check("Enter the radius of the circle: ", "Please enter a valid number (e.g., 4): ", float)

    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2

    perimeter = significant_figure(perimeter, 2)
    area = significant_figure(area, 2)

    return perimeter, area


def choice_oval():
    radius_horizontal = num_check("Enter the radius of the horizontal axis: ",
                                  "Please enter a valid number (e.g., 4): ", float)
    radius_vertical = num_check("Enter the radius of the vertical axis: ", "Please enter a valid number (e.g., 4): ",
                                float)

    perimeter = 2 * math.pi * (3 * (radius_horizontal + radius_vertical) - math.sqrt(
        (3 * radius_horizontal + radius_vertical) * (radius_horizontal + 3 * radius_vertical)))
    area = math.pi * radius_horizontal * radius_vertical

    perimeter = significant_figure(perimeter, 2)
    area = significant_figure(area, 2)

    return perimeter, area
