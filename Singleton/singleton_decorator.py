


def singleton(class_):
    instances = {}
    def wrapper(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args,**kwargs)
        return instances[class_]
    return wrapper

# this wrapper preserves that class is returned as it is not an object from it
# The decorator returns a callable function (wrapper), not the result of calling it.


@singleton
class Database:
    def __init__(self,name,age=0):
        print("Loading Data From Database!")

d1 = Database("ahmed")
d2 = Database("hamada")