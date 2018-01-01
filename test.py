def squared(arg):
    if isinstance(arg,int):
        return arg * arg
    elif arg.isdigit():
        arg = int(arg)
        return arg * arg
    else:
        return arg * len(arg)

print(squared(5))
print(squared("2"))
print(squared("tim"))
