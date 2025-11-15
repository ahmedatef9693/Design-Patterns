<<<<<<< HEAD
class Logger:
    def __init__(self, file_name=None):
        self.file_name = file_name

    def message(self, msg):
        print(msg)

class AdapterLogger:
    index = 0
    def __init__(self, logger: Logger, file_name="temp.txt"):
        self.logger = logger
        self.file_name = file_name
        
    def message(self, msg):
        self.logger.message(msg)
        with open(self.file_name, "a") as f:
            f.write(f"{self.index} : {msg} " +'\n')
        self.index+=1


log = Logger()
adapter = AdapterLogger(log, "output.txt")
adapter.message("Hello")
    


 
=======
class Logger:
    def __init__(self, file_name=None):
        self.file_name = file_name

    def message(self, msg):
        print(msg)

class AdapterLogger:
    index = 0
    def __init__(self, logger: Logger, file_name="temp.txt"):
        self.logger = logger
        self.file_name = file_name
        
    def message(self, msg):
        self.logger.message(msg)
        with open(self.file_name, "a") as f:
            f.write(f"{self.index} : {msg} " +'\n')
        self.index+=1


log = Logger()
adapter = AdapterLogger(log, "output.txt")
adapter.message("Hello")
    


 
>>>>>>> 2c05466 (adding new designs)
