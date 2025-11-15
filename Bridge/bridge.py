<<<<<<< HEAD
from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def draw(self):
#         pass

# #Complexity Explosion
# # class VectorCircle(Shape):
# #     def draw(self):
# #         print("VectorCircle")


# # class RasterCircle(Shape):
# #     def draw(self):
# #         print("RasterCircle")

# # class VectorRectangle(Shape):
# #     def draw(self):
# #         print("Rectangle")

# # class RasterRectangle(Shape):
# #     def draw(self):
# #         print("RasterRectangle")



class Renderer(ABC):
    def render_circle(self,radius):
        pass

    def render_rectangle(self,width,height):
        pass


class VectorRenderer(Renderer):
    def render_circle(self,radius):
        print(f'Drawing a circle of radius {radius}')

    def render_rectangle(self,width,height):
        print(f'Drawing a rectangle of width {width} and height {height}')

class RasterRenderer(Renderer):
    def render_circle(self,radius):
        print(f"Drawing pixels for a circle of radius {radius}")

    def render_rectangle(self,width,height):
        print(f'Drawing pixels for a rectangle of width {width} and height {height}')



class Shape:
    def __init__(self,renderer:Renderer = None):
        self.renderer = renderer
    
    def draw(self):pass
    def resize(self,factor):pass

class Circle(Shape):
    def __init__(self, renderer = None,radius:float=0.0):
        super().__init__(renderer)
        self.radius =radius

    def draw(self):
        self.renderer.render_circle(self.radius)
    def resize(self, factor):
        self.radius*=factor

raster = RasterRenderer()
vector = VectorRenderer()

circle = Circle(vector,2.3)
circle2 = Circle(raster,4.5)
circle.draw()
=======
from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def draw(self):
#         pass

# #Complexity Explosion
# # class VectorCircle(Shape):
# #     def draw(self):
# #         print("VectorCircle")


# # class RasterCircle(Shape):
# #     def draw(self):
# #         print("RasterCircle")

# # class VectorRectangle(Shape):
# #     def draw(self):
# #         print("Rectangle")

# # class RasterRectangle(Shape):
# #     def draw(self):
# #         print("RasterRectangle")



class Renderer(ABC):
    def render_circle(self,radius):
        pass

    def render_rectangle(self,width,height):
        pass


class VectorRenderer(Renderer):
    def render_circle(self,radius):
        print(f'Drawing a circle of radius {radius}')

    def render_rectangle(self,width,height):
        print(f'Drawing a rectangle of width {width} and height {height}')

class RasterRenderer(Renderer):
    def render_circle(self,radius):
        print(f"Drawing pixels for a circle of radius {radius}")

    def render_rectangle(self,width,height):
        print(f'Drawing pixels for a rectangle of width {width} and height {height}')



class Shape:
    def __init__(self,renderer:Renderer = None):
        self.renderer = renderer
    
    def draw(self):pass
    def resize(self,factor):pass

class Circle(Shape):
    def __init__(self, renderer = None,radius:float=0.0):
        super().__init__(renderer)
        self.radius =radius

    def draw(self):
        self.renderer.render_circle(self.radius)
    def resize(self, factor):
        self.radius*=factor

raster = RasterRenderer()
vector = VectorRenderer()

circle = Circle(vector,2.3)
circle2 = Circle(raster,4.5)
circle.draw()
>>>>>>> 2c05466 (adding new designs)
circle2.draw()