<<<<<<< HEAD



class Signleton:
    _instances = {}

    def __new__(cls,*args,**kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
            cls._instances[cls].initialized = False
        return cls._instances[cls]
    def __init__(self):
        if not self.initialized:
            print("loading daata")
            self.initialized = True


a = Signleton()
b = Signleton()
=======



class Signleton:
    _instances = {}

    def __new__(cls,*args,**kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
            cls._instances[cls].initialized = False
        return cls._instances[cls]
    def __init__(self):
        if not self.initialized:
            print("loading daata")
            self.initialized = True


a = Signleton()
b = Signleton()
>>>>>>> 2c05466 (adding new designs)
