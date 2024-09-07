
from enum import Enum

class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self,name,color,size):
        self.name = name
        self.color = color
        self.size = size



class ProductFilter:
    def filter_by_color(self,products,color):
        for product in products:
            if product.color == color:
                yield product

    def filter_by_size(self,products,size):
        for product in products:
            if product.size == size:
                yield product
    def filter_by_size_and_color(self,products,size,color):
        for product in products:
            if product.size == size and product.color == color:
                yield product




class Specification:
    def is_satisfied(self,item):
        pass
    def __and__(self,other):
        return AndSpecification(self,other)


class Filter:
    def filter(self,items,spec):
        pass



class ColorSpecification(Specification):
    def __init__(self,color):
        self.color = color

    def is_satisfiled(self,item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self,size):
        self.size = size
    def is_satisfiled(self,item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self,spec1,spec2):
        self.spec1 = spec1
        self.spec2 = spec2
    def is_satisfiled(self,item):
        return self.spec1.is_satisfiled(item) and self.spec2.is_satisfiled(item)


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfiled(item):
                yield item



products = [\
Product("Tree",Color.GREEN,Size.LARGE),\
Product("Apple",Color.RED,Size.SMALL) ,\
Product("Hat",Color.RED,Size.SMALL)\
]


and_specification = SizeSpecification(Size.LARGE) and ColorSpecification(Color.GREEN)
bf = BetterFilter()

for product in bf.filter(products,and_specification):
    print(f'products fit condition : {product.name}')





#old
# result = ProductFilter()
# for value in result.filter_by_color([p1, p2, p3],Color.RED):
#     print(value.name)

# for value in result.filter_by_size([p1, p2, p3],Size.SMALL):
#     print(value.name)

# for value in result.filter_by_size_and_color([p1, p2, p3],Size.SMALL,Color.RED):
#     print(value.name)










