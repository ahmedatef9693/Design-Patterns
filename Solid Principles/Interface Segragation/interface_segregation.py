
# abc stands for abstract based class
from abc import ABC,abstractmethod
# class Machine:
#     def print(self):
#         raise NotImplementedError
#     def scan(self):
#         raise NotImplementedError
#     def fax(self):
#         raise NotImplementedError




# abstract classes for methods
class Printer(ABC):
    def print_else(self):
        print("yes")
    @abstractmethod
    def print(self,document):
        pass
class Scanner(ABC):
    @abstractmethod
    def scan(self,document):
        pass
class Faxing(ABC):
    @abstractmethod
    def fax(self,user):
        pass


#Implementations
class MyPrinter(Printer):
    def print(self,document):
        print(f'printing document {document}!')


class MyScanner(Scanner):   
    def scan(self,document):
        print(f'scanning document {document}!')


class MyFax(Faxing):
    def fax(self,user):
        print(f'sending fax to user {user}!')







class OldMachine(Printer):
    def print(self,document):
        print(f"Old Machine Print {document}")




class PhotoCopier(Printer,Scanner):
    def print(self,document):
        print(f'PhotoCopier print {document}')
    def scan(self,document):
        print(f'PhotoCopier scan {document}')



#abstract machine can scan and fax
class MultifunctionDevice(Printer,Scanner):
    def scan(self,document):
        pass
    def fax(self,user):
        pass



class MultiFunctionMachine(MultifunctionDevice):
    def __init__(self,scanner,faxing,printer):
        self.scanner = scanner
        self.faxing = faxing
        self.printer = printer
    def scan(self,document):
        self.scanner.scan(document)
    def print(self,document):
        self.printer.print(document)
    def fax(self,user):
        self.faxing.fax(user)


mfm = MultiFunctionMachine(MyScanner(),MyFax(),MyPrinter())
mfm.scan("A")
mfm.print("A")
mfm.fax("Ahmed")


