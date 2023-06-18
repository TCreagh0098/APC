import math


# converts a number to a specified significant figure
def significant_figure(number, significant_figures):
    if number == 0:
        return 0
    return round(number, significant_figures - math.floor(math.log10(abs(number))) - 1)
