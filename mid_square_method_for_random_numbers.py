def mid_square_method(num, iterations):
    answers = []
    len_of_num = len(str(num))
    middle = len_of_num // 2
    for _ in range(iterations):
        x_squared = num**2
        if len_of_num % 2 == 0:
            middle_digits = str(x_squared)[middle - 1 : middle + 1]
            answers.append(int(middle_digits))
        elif len_of_num % 2 == 1:
            middle_digits = (str(x_squared))[middle]
            answers.append(int(middle_digits))
        num = x_squared
    return answers


if __name__ == "__main__":
    x0 = int(input("Enter the seed element "))
    no_of_iterations = int(input("Enter the no of iterations "))
    result = mid_square_method(x0, no_of_iterations)
    print(result)
