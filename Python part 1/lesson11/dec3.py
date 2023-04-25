def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return ret
    return wrapper

@benchmark
def fetch_web(url):
    import requests
    web = requests.get(url)
    return web.text

print(fetch_web("https://google.com"))
