def hello(name, prefix = "Hello, ", suffix = "!"):
    print("{}{}{}".format(prefix, name, suffix))

hello("World", "Hi ", "!!!!!!!")

def append_default(element, lst =[]):
    lst.append(element)
    return lst
print(append_default("1"))
print(append_default("2"))
print(append_default("3"))
print(append_default("4"))
