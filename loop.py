i = 3
while i != 0:
    print("Hello")
    i -= 1

for i in [0, 1, 2]:
    print("Meaw")

for _ in range(3):
    print("ok")

print("Dog\n"*3, end="")


def get_num():
    while True:
        n = int(input("What's n?"))
        if (n > 0):
            return n


def foo(n):
    for _ in range(n):
        print('Inside function\n', end="")


def main():
    value = get_num()
    foo(value)


# main()

students = ["hasib", "Hont", "jhon"]

# for student in students:
#     print(student)

for i in range(len(students)):
    print(students[i])

# dictinary-> dict


# single dictionary
dictinary = {
    "Hasib": "PSTU",
    "Badhon": "DU",
    "Urmee": "BU"
}

for student in dictinary:
    print(student, dictinary[student], sep=" | ")

# multi-dictionary
stu1 = [
    {"name": "Hasib", "house": "Dumkee", "Uni": "PSTU"},
    {"name": "Badhon", "house": "Patuakhali", "Uni": "BU"},
    {"name": "Tazim", "house": "Bhola", "Uni": "PSTU"},
]

for val in stu1:
    print(val["name"], val["house"],sep=", ")