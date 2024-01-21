print("\n".join([(lambda i: ("FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i)))(i) for i in range(1, 101)]))
