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