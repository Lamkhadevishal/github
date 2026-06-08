def add(a, b):
    """Add two numbers and return the result."""
    return a + b


if __name__ == "__main__":
    num1 = 10
    num2 = 20
    result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")



    for i in range(1,10):
        print(f"{num1} + {i} = {add(num1, i)}")
