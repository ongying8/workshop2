def myfunc():
    global x  # ประกาศ x = global
    x = "fantastic"


myfunc()
print("Python is " + x)