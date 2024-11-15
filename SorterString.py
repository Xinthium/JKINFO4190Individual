#To create a dynamic array in Python3, we are to use a "list".
list = []
while True:
    appendItem = input("Please provide a string(s) to the array.\nEntering 'exit' to stop the program and sort the Array.\n")
    if appendItem != "exit":
        list.append(appendItem)
    else:
        break
list.sort()
print(list)
