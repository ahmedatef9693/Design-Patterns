


def singleton(class_object):
    instances = {}
    def get_instance():
        if class_object not in instances:
            instances[class_object] = class_object()
        return instances[class_object]
    return get_instance




@singleton
class Database:
    def __init__(self,name=None):
        print("Loading Database")


d1 = Database()
d2 = Database()






