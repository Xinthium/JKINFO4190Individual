#To create a dynamic array in Python3, we are to use a "list".
list = []
while True:
    try:
        appendItem = int(input("Please provide a number to the array.\nEntering an invalid input will finalize the sorting and exit the program.\n"))
        list.append(appendItem)
    except:
        appendItem = "Invalid"
        if not list:
            print("That is not a valid input! Array is Empty!")
        else:
            print("That is not a valid input! Sorting Array!")
            list.sort()
            print(list)
            break
