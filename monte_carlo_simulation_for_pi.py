from random import random


def pi_using_monte_carlo(num_of_iterations, radius):

    inside = 0
    outside = 0
    for _ in range(num_of_iterations):
        x = random()
        y = random()
        if x**2 + y**2 <= radius**2:
            inside += 1
        else:
            outside += 1
    pi = 4 * (inside) / (inside + outside)
    return pi


if __name__ == "__main__":
    print(pi_using_monte_carlo(2000000, 1))
