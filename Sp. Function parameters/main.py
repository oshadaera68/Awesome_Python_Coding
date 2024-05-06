# slash parameter in python
def myfunction(p1, p2, /, p3):
    print(p1, p2, p3)


myfunction(10, 20, 30)
myfunction(10, 20, p3=30)


# myfunction(p1=10, p2=20, p3=30)
# myfunction(10, p2=20, p3=30)
# myfunction(p1=10, 20, 30)

# slash parameter in python
def myfunction2(p1, p2, *, p3):
    print(p1, p2, p3)


# myfunction2(10, 20, 30)
myfunction2(p1=10, p2=20, p3=30)


def myfunction3(p1, /, p2, *, p3):
    print(p1, p2, p3)


# myfunction3(10, p2=20, 30)
myfunction3(10, 20, p3=30)
