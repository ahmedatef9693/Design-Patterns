from abc import ABC,abstractmethod


class Box(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def calculate_price(self):
        pass
        
class CompositeBox(Box):
    def __init__(self,boxes:list[Box]=[]):
        self.boxes = boxes
    def calculate_price(self):
        total = 0
        for box in self.boxes:
            total+= box.calculate_price()
        return total

class Product(Box):
    def __init__(self,price:float,title:str):
        self.price = price
        self.title = title

    def calculate_price(self) -> float:
        return self.price

class Book(Product):
    def __init__(self,price:float,title:str):
        super().__init__(price,title)

class VideoGame(Product):
    def __init__(self,price:float,title:str):
        super().__init__(price,title)

class DeliveryService:
    def __init__(self):
        self.box = None
    def setup_order(self,boxes:list[Box]):
        self.box = CompositeBox(boxes)

    def calculate_order_price(self):
        return self.box.calculate_price()


delivery_service = DeliveryService()
delivery_service.setup_order([
    Book(4.5,"sheakspear"),
    VideoGame(1000,"Fifa"),
    CompositeBox([
        Book(2.2,"romance"),
        VideoGame(2000,"Pes")
        ])
    ])
print(delivery_service.calculate_order_price())
