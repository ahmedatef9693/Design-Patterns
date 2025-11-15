
def counting_closure(func):
    index = 0
    def wrapper(*args,**kargs):
        nonlocal index

        print(*args)
        print(index)
        func(*args,**kargs)
        index+=1


    
    return wrapper


@counting_closure
def updates(data):
    pass


updates("as")
updates("fg")
updates("hh")