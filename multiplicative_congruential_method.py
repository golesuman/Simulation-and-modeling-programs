def mulitiplicative_congruential_method(a, x, m, n):
    result = []
    for _ in range(n):
        x = (a * x) % m
        result.append(x)

    return result

if __name__ == "__main__":
    result = mulitiplicative_congruential_method(1103515245, 1, 31**2, 10)
    print(result)
