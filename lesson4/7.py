#def hello(name, prefix = "Hello, ", suffix = "!"):
    #print("{}{}{}".format(prefix, name, suffix))

#hello(prefix="Hi", name="world")

#**kwargd
#*args

def printc(arg1, arg2, *args, **kwargs):
    print(" ".join([arg1] + [arg2] + list(args) + list(kwargs.values())))

printc('1', '2', '3', four='4', five='5')

