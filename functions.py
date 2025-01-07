def wish_greetings(name):
    print("Good Morning",name)

wish_greetings("Sudheesh")

def print_name_and_age(name, age):
    print("Your name is", name, "and my age is", age)

print_name_and_age("Sudheesh", 34)

def print_dynamic_vars(*args):
    print(args)
    print(type(args)) # tupple

print_dynamic_vars("Sudheesh", 34, "Python", 3.14)