print(" ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python ")

def display_main_menu():
    print("main menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    get_user_input()

def get_user_input():

    userinput = input().split(",")
    userinput = [float(item) for item in userinput]
    print(userinput)
    calc_average(userinput)
    find_min_max(userinput)

def calc_average(data):
    total = sum(data)
    avg = total / len(data)
    print("The avg is: " + str(avg))

def find_min_max(data):
    dmax = max(data)
    dmin = min(data)
    print("Min is: " + str(dmin) + "Max is: " + str(dmax))

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

display_main_menu()