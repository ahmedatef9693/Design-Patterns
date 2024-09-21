from enum import Enum
from abc import abstractmethod
class Relationship(Enum):
    Parent = 0
    Child = 1
    Sibling = 2



class Person:
    def __init__(self,name):
        self.name = name



class RelationshipBrowser:
    @abstractmethod
    def find_children_of(self,name):pass
    

class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_child(self,parent,child):
        self.relations.append((parent,Relationship.Parent,child))
    
    def find_children_of(self, name):
        for relation in self.relations:
            if relation[0].name == name and relation[1] == Relationship.Parent:
                yield relation[2].name



""" 
    Higer Module Must Not Depend on Lower Module 
    (Or Concrete Impementation Of Lower Module)
    Because 
    Lower Module Data Structure Could Change
    Rather Than That It Should Depend On Abstraction
"""
class Research:
    def __init__(self,relationships):
        for p in relationships.find_children_of("John"):
            print(p)


parent = Person("John")
child1 = Person("Tom")
child2 = Person("Smith")

relations = Relationships()
relations.add_parent_child(parent,child1)
relations.add_parent_child(parent,child2)
Research(relations)
