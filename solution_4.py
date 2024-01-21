print("\n".join([(lambda i: "Fizz"*(i%3==0) + "Buzz"*(i%5==0) or str(i))(i) for i in range(1, 101)]))
