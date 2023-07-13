file = open("devices.txt", "a")
while True:
    op = input("Enter device name: ")
    if op=="exit":
        print("All Done")
        break
    file.write(op + "\n")
file.close()
