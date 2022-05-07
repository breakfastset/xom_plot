import math

def solve_quadratic_equation(a, b, c):
    numerator_one = -1 * b + math.sqrt(b * b - 4 * a * c)
    numerator_two = -1 * b - math.sqrt(b * b - 4 * a * c)
    denominator = 2 * a

    solution_one = numerator_one / denominator
    solution_two = numerator_two / denominator

    return solution_one, solution_two    # return 2 solutions


def main():
    # x^2 - 7x + 10 = 0
    # ax^2 + bx + c = 0
    # a = 1,   b = -7,    c = 10
    a = 1
    b = -7
    c = 10
    x1, x2 = solve_quadratic_equation(a, b, c)

    print(f"Solutions are {x1} and {x2}")

main()