name=input("What's your name? ")

with open("name.txt","a") as file:
    file.write(f"{name}\n")