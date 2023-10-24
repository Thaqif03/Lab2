print(" ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python ")

def display_main_menu():
    print("main menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    get_user_input()

def get_user_input():

    userinput = input().split(",")
    userinput = [float(item) for item in userinput]
    print(userinput)

def calc_average():
    print("calc_average")

def find_min_max():
    print("find_min_max")

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

display_main_menu()