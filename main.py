# x = float(input("what is x? "))
# y = float(input("What is y? "))

# z = x+y
# # f string
# print(f"{z:,}")

# name=input("What's your name?")

# # print(f"hello, {name}")

# def foo(name="Sherhan"):
#     print("hello, ", name)


# foo()
# foo(name)

def main():
    x = int(input("Whats is x? "))
    print("x square is : ", square(x))


def square(x):
    return x*x

main()