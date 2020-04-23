__author__ = 'Keshan De Silva'
# f(x) = x^2 + 5^x - 3


def calculate_fx(arg_x):
    return arg_x * arg_x + 5 * arg_x - 3


def calculate_gx(arg_x):
    return 2 * arg_x + 5


MAX_ITERATIONS = 1000
EPSILON = 1.0e-3
INITIAL_VALUE = 1.0

x = INITIAL_VALUE
fx = calculate_fx(x)
gx = calculate_fx(x)
previous_fx = float("inf")
iteration = 0

while abs(fx - previous_fx) > EPSILON and iteration < MAX_ITERATIONS:
    previous_fx = fx
    x -= fx / gx

    fx = calculate_fx(x)
    gx = calculate_fx(x)

    iteration += 1

    # Display Information
    print("Iteration = " + str(iteration) + " x = " + str(x) + " f(x) = " + str(fx))

print("Minimum Value Found")
print(" x = " + str(x) + " f(x) = " + str(fx))