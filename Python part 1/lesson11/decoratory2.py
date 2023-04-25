"""def decorator_function(func):
    def wrapper():
        print("Wrapper function")
        print("Function that was wrapped: {}".format(func))
        print("Starting function that was wrapped")
        func()
        print("Exit from wrapper")
    return wrapper

@decorator_function
def hello_world():
    print("Hello world")
hello_world()"""

def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return wrapper

@benchmark
def fetch_web():
    import requests
    web = requests.get("https://google.com")

fetch_web()