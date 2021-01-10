x = "awesome"  # X ใน gobal


def myFunc():
    x = "fantastic"  # X ใน ฟังก์ชั่น
    print("[-] Pythin is " + x)


myFunc()
print("Python is " + x)


# Output
# [-] Pythin is fantastic
# Python is awesome
