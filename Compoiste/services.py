from abc import ABC, abstractmethod

class ServiceComponent(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def get_delivery_time(self) -> int:
        pass


class Service(ServiceComponent):
    def __init__(self, name: str, price: float, delivery_days: int):
        self.name = name
        self.price = price
        self.delivery_days = delivery_days

    def get_price(self) -> float:
        return self.price
        

    def get_delivery_time(self) -> int:
        return self.delivery_days


class ServicePackage(ServiceComponent):
    def __init__(self, name: str,services:list[ServiceComponent]):
        self.name = name
        self.services: list[ServiceComponent] = services

    def add_service(self, service: ServiceComponent):
        self.services.append(service)


    def get_price(self) -> float:
        total_price = 0
        for service in self.services:
            total_price += service.get_price()
        return total_price

    def get_delivery_time(self) -> int:
        total_delivery_time = 0
        for service in self.services:
            total_delivery_time += service.get_delivery_time()
        return total_delivery_time

    def show_details(self, indent=0):
        print(" " * indent + f"Package: {self.name}")
        for service in self.services:
            if isinstance(service, ServicePackage):
                service.show_details(indent + 2)
            else:
                print(" " * (indent + 2) + f"- {service.name}: ${service.price}, {service.delivery_days} days")



if __name__ == "__main__":
    ui = Service("UI Design", 500, 3)
    backend = Service("Backend Setup", 1000, 7)
    deploy = Service("Deployment", 300, 2)

    app_package = ServicePackage("Full App Development",[
        ui,Service("s1",4.5,5),Service("s2",4.5,5),ServicePackage("SS",[Service("a",2,4)])
    ])
    app_package.add_service(Service("s3",4.5,5))
    app_package.add_service(Service("s4",4.5,5))
    app_package.show_details()
    print("Total Price:", app_package.get_price())
    print("Total Delivery Time:", app_package.get_delivery_time())
