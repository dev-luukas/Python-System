import random

Option = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
          "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "§", "%", "&", "/", "=", ".", "-", ",", "*"]

try:
    UserInput = int(input("Please select how many digits your password should have: "))
    
    if UserInput <= 0:
        print("ERROR: Your password must have more than 0 characters!")
    else:
        password = "".join(random.choice(Option) for _ in range(UserInput))
        print(f"Your password: {password}")

except ValueError:
    print("ERROR: Please enter a valid number!")
