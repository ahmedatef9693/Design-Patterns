import time
def timeit(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(args,kwargs)
        end = time.time()
        print(f"{(end-start)*1000} ms")
    return wrapper
@timeit
def some_operation(*args,**kwargs):
    print("Starting...")
    time.sleep(1)
    print("Executed")
    



some_operation()