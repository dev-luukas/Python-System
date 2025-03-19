import socket

Choice = input("Do you want to get your IP (Y/N): ")

host = socket.gethostname()
ip = socket.gethostbyname(host)

if Choice == "Y" or Choice == "y":
    print(ip)
elif Choice == "N" or Choice == "n":
    print("Program is closing")
else:
    print("Invalid input, please enter Y or N.")
