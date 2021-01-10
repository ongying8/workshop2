x = "awesome"


def myFunc():
    global x
    # x = awesome
    print("Python is " + x)
    x = "fantastic"
    # x = fantastic


ongying
myFunc()
print("Python is " + x)

# Output
# Python is awesome
# Python is fantastic