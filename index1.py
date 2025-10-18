def volboite(x1=None,x2=None,x3=None):
    if x1 is None:
        return -1
    elif x2 is None:
        return x1**3
    elif x3 is None:
        return (x1**2)*x2
    else:
        return x1*x2*x3
print(volboite())
print(volboite(5.2))
print(volboite(5.2,3))
print(volboite(5.2,3,7.4))