






class Singleton(type):
    _instances = {}
    def __call__(self,*args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Singleton, self).__call__(*args, **kwargs)
        return self._instances[self]
        





class Database(metaclass = Singleton):
    def __init__(self):
        print("Loading Database!")


d1 = Database()
d2 = Database()

print(d1 == d2)