class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, entry):
        self.entries.append(f"{self.count+1}: {entry}")
        self.count += 1
    
    def remove_entry(self, pos):
        if pos < 0 or pos >= self.count:
            print("Invalid position!")
            return
        del self.entries[pos]
        self.count -= 1

    def display(self):
        for entry in self.entries:
            print(entry)

    # def save(self,filename):
    #     file = open(filename,"w")
    #     file.write(str(self.entries))
    #     file.close()


    


