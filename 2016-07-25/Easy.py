fraction = [4, 8]
#find simplest fraction [1, 2]

def simplest_fraction(fraction_list):
    divider = 2
    x, y = fraction_list
    while divider <= x and divider <= y:
        x_temp, y_temp = (x/divider), (y/divider)
        print(x_temp,y_temp)
        if x_temp.is_integer() and y_temp.is_integer():
            print("if")
            x, y = x_temp, y_temp
        divider += 1

    return x,y




print(simplest_fraction([4,8]))
