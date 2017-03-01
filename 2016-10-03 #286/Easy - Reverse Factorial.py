def factorial():
    answer = 1
    count = 1
    while True:
        yield answer
        count += 1
        answer *= count

# func = factorial()
# print(func)
# for v in range(5):
#     print(func.__next__())

def reverse_factorial(value):
    func = factorial()
    factorial_guess = func.__next__()
    counter = 1
    while value > factorial_guess:
        counter += 1
        factorial_guess = func.__next__()
    if value == factorial_guess:
        print("{} = {}!".format(value,counter))
    else:
        print('None')


reverse_factorial(479001600)

