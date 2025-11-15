class House:
    def __init__(self,builder):
        self.stories = builder.stories
        self.roof_type = builder.roof_type
        self.door_type = builder.door_type


print("helo world")

#Construction Of An Object Separated From The Representation
class HouseBuilder:
    def __init__(self):
        self.stories = None
        self.roof_type = None
        self.door_type = None

    def set_stories(self,stories):
        self.stories = stories
        return self
    def set_rooftype(self,rooftype):
        self.roof_type = rooftype
        return self
    def set_door_type(self,door_type):
        self.door_type = door_type
        return self
    
    def build(self):
        return House(self)


#director is the class that manages the builder
class Director:
    def __init__(self,builder):
        self.builder = builder

    def build_one_story_houses(self):
        return self.builder.set_stories(1).set_rooftype("Pointy").set_door_type("Single").build()

    def build_two_story_houses(self):
        return self.builder.set_stories(2).set_rooftype("Flat").set_door_type("Double").build()


house_builder = HouseBuilder()
director = Director(house_builder)
print(director.build_one_story_houses().stories)
print(director.build_two_story_houses().stories)