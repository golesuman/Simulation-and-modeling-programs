def generate_random_numbers(x_init, a, c, m):
    random_numbers = []
    for _ in range(10):
        x_1 = (a * x_init + c) % m
        r = x_1 / m
        random_numbers.append(r)
        x_init = x_1
    return random_numbers


if __name__ == "__main__":
    random_result = generate_random_numbers(27, 17, 43, 100)
    print(random_result)
