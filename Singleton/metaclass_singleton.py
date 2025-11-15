
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args,**kwds)
        return cls._instances[cls]
    


class Database(metaclass= Singleton):
    def __init__(self):
        print("Loading Database")



d1 = Database()
d2 = Database()

        


