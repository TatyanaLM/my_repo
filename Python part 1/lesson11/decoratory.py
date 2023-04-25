def hello_world():
    print("Hello world")

print(type(hello_world))


def wrapper_function():
    def hello_world():
        print("Hello world")
    hello_world()

wrapper_function()

def higher_order(func):
    print("Got function {} as arg".format(func))
    func()
    return(func)

higher_order(hello_world)