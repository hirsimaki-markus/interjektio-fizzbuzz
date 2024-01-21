def fizzbuzz():
    output = ""
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            output += "FizzBuzz\n"
        elif num % 3 == 0:
            output += "Fizz\n"
        elif num % 5 == 0:
            output += "Buzz\n"
        else:
            output += str(num) + "\n"
    return output[:-1]


if __name__ == "__main__":
    print(fizzbuzz())
