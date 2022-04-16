def first_method():
    second_method()
    print("i'm first method")
def second_method():
    third_method()
    print("i'm second method")
def third_method():
    fourth_method()
    print("i'm third method")
def fourth_method():
    print("i'm fourt method")

first_method()